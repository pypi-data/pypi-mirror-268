import json

from sklearn.utils import Bunch

from ..utils.encoding import NumpyEncoder
from ..utils.params import checkInstance


class _Result(Bunch):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def toJson(self, indent=None, compressed=False):
        # compressed is not used at the moment
        return json.dumps(self, cls=NumpyEncoder, indent=indent)


class EnsemblePartialResult(_Result):
    def __init__(
        self, info=None, metrics=None, centroids=None, labels=None, partitions=None, runsStatus=None, taskId=None
    ):
        super().__init__(
            info=checkInstance(info, EnsemblePartialResultInfo, "info"),
            earlyTermination=EnsemblePartialResultEarlyTermination(),
            metrics=checkInstance(metrics, EnsemblePartialResultMetrics, "metrics"),
            centroids=centroids,
            labels=labels,
            partitions=partitions,
            runsStatus=checkInstance(runsStatus, EnsemblePartialResultRunsStatus, "runsStatus"),
            taskId=taskId,
        )

    def _setEarlyTermination(self, name, boolean):
        self.earlyTermination[name] = boolean


class EnsemblePartialResultInfo(_Result):
    def __init__(self, ensembleId, iteration, seed, last, completed, cost, bestRun, inertia):
        super().__init__(
            id=ensembleId,
            iteration=iteration,
            seed=seed,
            last=last,
            completed=completed,
            cost=cost,
            bestRun=bestRun,
            inertia=inertia,
        )


class EnsemblePartialResultRunsStatus(_Result):
    def __init__(self, runIteration=None, runCompleted=None, runsKilled=None):
        super().__init__(runIteration=runIteration, runCompleted=runCompleted, runsKilled=runsKilled)


class MetricGroup(_Result):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class EnsemblePartialResultMetrics(_Result):
    def __init__(
        self,
        labelsValidationMetrics=None,
        labelsComparisonMetrics=None,
        labelsProgressionMetrics=None,
        partitionsValidationMetrics=None,
        partitionsComparisonMetrics=None,
        partitionsProgressionMetrics=None,
    ):
        super().__init__(
            labelsValidationMetrics=checkInstance(labelsValidationMetrics, MetricGroup, "labelsValidationMetrics"),
            labelsComparisonMetrics=checkInstance(labelsComparisonMetrics, MetricGroup, "labelsComparisonMetrics"),
            labelsProgressionMetrics=checkInstance(labelsProgressionMetrics, MetricGroup, "labelsProgressionMetrics"),
            partitionsValidationMetrics=checkInstance(
                partitionsValidationMetrics, MetricGroup, "partitionsValidationMetrics"
            ),
            partitionsComparisonMetrics=checkInstance(
                partitionsComparisonMetrics, MetricGroup, "partitionsComparisonMetrics"
            ),
            partitionsProgressionMetrics=checkInstance(
                partitionsProgressionMetrics, MetricGroup, "partitionsProgressionMetrics"
            ),
        )


class EnsemblePartialResultEarlyTermination(_Result):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
