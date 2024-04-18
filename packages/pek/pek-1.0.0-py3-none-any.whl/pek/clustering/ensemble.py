import time

import numpy as np

from pek.termination.earlyTermination import EarlyTerminationAction

from ..data import DatasetLoader
from ..metrics.comparison import (
    checkComparisonMetrics,
    getComparisonMetricFunctionByName,
)
from ..metrics.progression import (
    checkProgressionMetrics,
    getProgressionMetricFunctionByName,
)
from ..metrics.validation import (
    checkValidationMetrics,
    getValidationMetricFunctionByName,
)
from ..utils.clustering import adjustCentroids_fn, adjustLabels_fn
from .interfaces import _ProgressiveEnsembleKMeansInterface
from .results import (
    EnsemblePartialResult,
    EnsemblePartialResultInfo,
    EnsemblePartialResultMetrics,
    EnsemblePartialResultRunsStatus,
    MetricGroup,
)
from .run import ProgressiveKMeans


class ProgressiveEnsembleKMeans(_ProgressiveEnsembleKMeansInterface):
    """
    A class representing a progressive ensemble K-means algorithm.

    Parameters:
    - data: string, array-like or sparse matrix. The input data. In case of string, pass a string compatible with pek.data.DatasetLoader.loadDataMatrix(data).
    - n_clusters: int, default=2. The number of clusters.
    - n_runs: int, default=4. The number of concurrent runs.
    - init: str, default="k-means++". The initialization method for centroids.
    - max_iter: int, default=300. The maximum number of iterations.
    - tol: float, default=1e-4. Tolerance to declare convergence.
    - random_state: random_state, optional. Seed for random number generation.
    - freq: float or None, default=None. The minimum frequency in seconds between two progressive results.
    - ets: default None. Early terminators list.
    - labelsValidationMetrics
    - labelsComparisonMetrics
    - labelsProgressionMetrics
    - partitionsValidationMetrics
    - partitionsComparisonMetrics
    - partitionsProgressionMetrics
    - adjustCentroids: bool, default=Tru. Whether to adjust centroids during iterations to minimize differences.
    - adjustLabels: bool, default=True. Whether to adjust labels during iterations.
    - returnPartitions: bool, default=True. Whether to return partitions on each partial result.
    - taskId: any, default=None. Identifier for the task.
    """

    def __init__(
        self,
        data=None,
        n_clusters=2,
        n_runs=4,
        init="k-means++",
        max_iter=300,
        tol=1e-4,
        random_state=None,
        freq=None,
        ets=None,
        labelsValidationMetrics=None,
        labelsComparisonMetrics=None,
        labelsProgressionMetrics=None,
        partitionsValidationMetrics=None,
        partitionsComparisonMetrics=None,
        partitionsProgressionMetrics=None,
        adjustCentroids=True,
        adjustLabels=True,
        returnPartitions=True,
        **kwargs
    ):
        super().__init__(
            data=data,
            n_clusters=n_clusters,
            n_runs=n_runs,
            init=init,
            max_iter=max_iter,
            tol=tol,
            random_state=random_state,
            freq=freq,
            ets=ets,
            labelsValidationMetrics=labelsValidationMetrics,
            labelsComparisonMetrics=labelsComparisonMetrics,
            labelsProgressionMetrics=labelsProgressionMetrics,
            partitionsValidationMetrics=partitionsValidationMetrics,
            partitionsComparisonMetrics=partitionsComparisonMetrics,
            partitionsProgressionMetrics=partitionsProgressionMetrics,
            adjustCentroids=adjustCentroids,
            adjustLabels=adjustLabels,
            returnPartitions=returnPartitions,
            **kwargs
        )

        self._X = None
        if isinstance(self._data, str):
            self._X = DatasetLoader.loadX(self._data)
        else:
            self._X = self._data

        self._iteration = -1
        self._completed = False
        self._killed = False
        self._runs = []

        self._prevResultCentroids = None
        self._prevResultTimestamp = 0.0

        # create run objects
        for i, seed in enumerate(
            np.random.default_rng(self._random_state).integers(0, np.iinfo(np.int32).max, size=self._n_runs)
        ):
            r = ProgressiveKMeans(
                self._X,
                n_clusters=self._n_clusters,
                max_iter=self._max_iter[i],
                tol=self._tol[i],
                random_state=seed,
                init=self._init[i],
            )
            self._runs.append(r)

        # adjust the order of centroids in the runs
        # to have the same label assigned to a similar part of the space
        # this limit the problem of consistency among different partitions
        if self._adjustCentroids:
            adjustCentroids_fn(self._runs)

        self._partitions = np.zeros((self._n_runs, self._X.shape[0]), dtype=int)
        self._centroids = np.zeros((self._n_clusters, self._X.shape[1], self._n_runs), dtype=float)
        self._runsLastPartialResultInfo = [None for _ in range(self._n_runs)]
        self._runsLastPartialResultMetrics = [None for _ in range(self._n_runs)]
        self._runsIteration = [None for _ in range(self._n_runs)]
        self._runsCompleted = [False for _ in range(self._n_runs)]
        self._runsKilled = [False for _ in range(self._n_runs)]
        self._runsInertia = [np.inf for _ in range(self._n_runs)]
        self._disabledEts = [False for _ in self._ets]

        self._metricsManager = _EnsembleMetricsManager(
            self._X,
            self._labelsValidationMetrics,
            self._labelsComparisonMetrics,
            self._labelsProgressionMetrics,
            self._partitionsValidationMetrics,
            self._partitionsComparisonMetrics,
            self._partitionsProgressionMetrics,
        )

    def _executeNextIteration(self) -> EnsemblePartialResult:
        if not self.hasNextIteration():
            raise RuntimeError("No next iteration to execute.")

        # compute an iteration of each run
        iterationCost = 0
        for i in range(self._n_runs):
            if self._runs[i].hasNextIteration():
                iterationCost += 1
                rp = self._runs[i].executeNextIteration()
                self._partitions[i, :] = rp.labels
                self._centroids[:, :, i] = rp.centroids
                self._runsLastPartialResultInfo[i] = rp.info
                self._runsLastPartialResultMetrics[i] = rp.metrics
                self._runsCompleted[i] = rp.info.isLast
                self._runsInertia[i] = rp.metrics.inertia
                self._runsIteration[i] = rp.info.iteration

        self._iteration += 1
        self._completed = np.all([not self._runs[j].hasNextIteration() for j in range(self._n_runs)])

        # choose the champion
        bestRunIndex = int(np.argmin(self._runsInertia))
        bestCentroids = self._centroids[:, :, bestRunIndex]
        bestLabels = self._partitions[bestRunIndex, :]
        bestInertia = float(self._runsInertia[bestRunIndex])

        # minimize label changing
        if self._adjustLabels and self._prevResultCentroids is not None:
            for i in range(self._n_runs):
                self._partitions[i, :] = adjustLabels_fn(
                    self._partitions[i, :], bestCentroids, self._prevResultCentroids
                )
                # self._partitions[bestRunIndex, :] = adjustLabels(bestLabels, bestCentroids, self._prevResultCentroids)
            bestLabels = self._partitions[bestRunIndex, :]

        # create the partial result (info)
        last = not self.hasNextIteration()

        ensemblePartialResultInfo = EnsemblePartialResultInfo(
            self._id,
            self._iteration,
            self._random_state,
            last,
            self._completed,
            iterationCost,
            bestRunIndex,
            bestInertia,
        )

        # runsStatus
        runIteration_str = "-".join(map(str, np.array(self._runsIteration).astype(int)))
        runCompleted_str = "-".join(map(str, np.array(self._runsCompleted).astype(int)))
        runsKilled_str = "-".join(map(str, np.array(self._runsKilled).astype(int)))
        runsStatus = EnsemblePartialResultRunsStatus(
            runIteration=runIteration_str, runCompleted=runCompleted_str, runsKilled=runsKilled_str
        )

        # create the partial result (metrics)
        metrics = self._metricsManager.computeMetrics(
            bestRunIndex, self._runsInertia, self._centroids, self._partitions
        )

        # create the partial result
        ensemblePartialResult = EnsemblePartialResult(
            info=ensemblePartialResultInfo,
            metrics=metrics,
            centroids=bestCentroids,
            labels=bestLabels,
            partitions=self._partitions if self._returnPartitions else None,
            runsStatus=runsStatus,
            taskId=self._taskId,
        )

        # manage the early termination
        for i, et in enumerate(self._ets):
            if self._disabledEts[i]:
                continue
            action = et.checkEarlyTermination(ensemblePartialResult)
            if action == EarlyTerminationAction.NONE:
                continue
            elif action == EarlyTerminationAction.NOTIFY:
                self._disabledEts[i] = True
                ensemblePartialResult._setEarlyTermination(et.name, True)
            elif action == EarlyTerminationAction.KILL:
                self._disabledEts[i] = True
                ensemblePartialResult._setEarlyTermination(et.name, True)
                ensemblePartialResult.info.last = True
                self.kill()

        # manage results frequency
        currentTimestamp = time.time()
        elapsedFromPrevPartialResult = currentTimestamp - self._prevResultTimestamp
        if (self._freq is not None) and (elapsedFromPrevPartialResult < self._freq):
            time.sleep(self._freq - elapsedFromPrevPartialResult)

        # update previous result
        self._prevResultCentroids = bestCentroids
        self._prevResultTimestamp = time.time()

        # return the current partial result
        return ensemblePartialResult

    def hasNextIteration(self) -> bool:
        """Checks if there are more iterations to execute."""
        return not self._completed and not self._killed

    def executeNextIteration(self) -> EnsemblePartialResult:
        """Executes the next iteration. Raises a RuntimeError if there are no more iterations to execute.
        Returns the EnsemblePartialResult produced in the iteration."""
        return self._executeNextIteration()

    def executeAllIterations(self) -> EnsemblePartialResult:
        """Executes all the remaining iterations. Returns the last produced EnsemblePartialResult."""
        r = None
        while self.hasNextIteration():
            r = self.executeNextIteration()
        return r

    def kill(self):
        """Kills the ensemble, as a consequence there are no more iterations to execute."""
        self._killed = True

    def killRun(self, run):
        """Kills a specified run."""
        self._runsKilled[run] = True
        self._runs[run].kill()

    # def


########################################################################################################################
########################################################################################################################
########################################################################################################################


class _EnsembleMetricsManager:
    def __init__(
        self,
        X,
        labelsValidationMetrics,
        labelsComparisonMetrics,
        labelsProgressionMetrics,
        partitionsValidationMetrics,
        partitionsComparisonMetrics,
        partitionsProgressionMetrics,
    ):
        self._X = X

        self._labelsValidationMetrics = checkValidationMetrics(labelsValidationMetrics)
        self._labelsComparisonMetrics = checkComparisonMetrics(labelsComparisonMetrics)
        self._labelsProgressionMetrics = checkProgressionMetrics(labelsProgressionMetrics)

        self._partitionsValidationMetrics = checkValidationMetrics(partitionsValidationMetrics)
        self._partitionsComparisonMetrics = checkComparisonMetrics(partitionsComparisonMetrics)
        self._partitionsProgressionMetrics = checkProgressionMetrics(partitionsProgressionMetrics)

        self._bestLabelsPrev = None
        self._labelsHistory = []
        self._partitionsHistory = []

    def computeMetrics(self, bestRunIndex, runsInertia, centroids, partitions) -> EnsemblePartialResultMetrics:
        return EnsemblePartialResultMetrics(
            labelsValidationMetrics=self._compute_labelsValidationMetrics(
                bestRunIndex, runsInertia, centroids, partitions
            ),
            labelsComparisonMetrics=self._compute_labelsComparisonMetrics(
                bestRunIndex, runsInertia, centroids, partitions
            ),
            labelsProgressionMetrics=self._compute_labelsProgressionMetrics(
                bestRunIndex, runsInertia, centroids, partitions
            ),
            partitionsValidationMetrics=self._compute_partitionsValidationMetrics(
                bestRunIndex, runsInertia, centroids, partitions
            ),
            partitionsComparisonMetrics=self._compute_partitionsComparisonMetrics(
                bestRunIndex, runsInertia, centroids, partitions
            ),
            partitionsProgressionMetrics=self._compute_partitionsProgressionMetrics(
                bestRunIndex, runsInertia, centroids, partitions
            ),
        )

    def _compute_labelsValidationMetrics(self, bestRunIndex, runsInertia, centroids, partitions):
        """Labels validation metrics are computed only on the current best labels."""
        bestInertia = float(runsInertia[bestRunIndex])
        bestLabels = partitions[bestRunIndex, :]

        res = {"inertia": bestInertia}
        for metricName in self._labelsValidationMetrics:
            if metricName not in res:
                res[metricName] = getValidationMetricFunctionByName(metricName)(self._X, bestLabels)

        return MetricGroup(**res)

    def _compute_labelsComparisonMetrics(self, bestRunIndex, runsInertia, centroids, partitions):
        """Labels comparison metrics are computed comparing the current best labels with the previous best labels.
        The initial iteration is Null"""
        bestLabels = partitions[bestRunIndex, :]

        res = {}
        for metricName in self._labelsComparisonMetrics:
            if metricName not in res:
                if self._bestLabelsPrev is None:
                    res[metricName] = None
                else:
                    res[metricName] = getComparisonMetricFunctionByName(metricName)(bestLabels, self._bestLabelsPrev)

        if len(self._labelsComparisonMetrics) > 0:
            self._bestLabelsPrev = bestLabels

        return MetricGroup(**res)

    def _compute_labelsProgressionMetrics(self, bestRunIndex, runsInertia, centroids, partitions):
        if len(self._labelsProgressionMetrics) > 0:
            self._labelsHistory.append(partitions[bestRunIndex, :])

        res = {}
        for metricName in self._labelsProgressionMetrics:
            if metricName not in res:
                res[metricName] = getProgressionMetricFunctionByName(metricName)(self._labelsHistory)

        return MetricGroup(**res)

    def _compute_partitionsValidationMetrics(self, bestRunIndex, runsInertia, centroids, partitions):
        """Partitions validation metrics are computed on each partition.
        The result is a dictionary where each metric has an array of values, one for each partition.
        """
        res = {"inertia": runsInertia}
        for metricName in self._partitionsValidationMetrics:
            if metricName not in res:
                res[metricName] = np.empty(partitions.shape[0], dtype=float)
                for i in range(partitions.shape[0]):
                    res[metricName][i] = getValidationMetricFunctionByName(metricName)(self._X, partitions[i, :])

        return MetricGroup(**res)

    def _compute_partitionsComparisonMetrics(self, bestRunIndex, runsInertia, centroids, partitions):
        """
        Partitions comparison metrics are computed on each pair of partition.
        The result is a dictionary where each metric has a symmetric matrix RxR.
        """
        n_runs = partitions.shape[0]
        res = {}
        for metricName in self._partitionsComparisonMetrics:
            if metricName not in res:
                res[metricName] = np.empty((n_runs, n_runs), dtype=float)

                for i in range(n_runs):
                    for j in range(n_runs):
                        if j >= i:
                            continue
                        val = getComparisonMetricFunctionByName(metricName)(partitions[i, :], partitions[j, :])
                        res[metricName][i, j] = val
                        res[metricName][j, i] = val

        return MetricGroup(**res)

    def _compute_partitionsProgressionMetrics(self, bestRunIndex, runsInertia, centroids, partitions):
        if len(self._partitionsProgressionMetrics) > 0:
            self._partitionsHistory.append(partitions)

        n_runs = partitions.shape[0]
        res = {}
        for metricName in self._partitionsProgressionMetrics:
            if metricName not in res:
                res[metricName] = [None for j in range(n_runs)]
                for i in range(n_runs):
                    # if len(self._partitionsHistory) > 1:
                    hist = [p[i, :] for p in self._partitionsHistory]
                    res[metricName][i] = getProgressionMetricFunctionByName(metricName)(hist)

        return MetricGroup(**res)
