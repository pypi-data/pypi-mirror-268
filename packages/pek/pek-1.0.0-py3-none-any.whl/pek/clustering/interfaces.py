import uuid
from abc import ABC, abstractmethod

from sklearn.utils._param_validation import Integral, Interval, Real, validate_params

from ..metrics.comparison import checkComparisonMetrics
from ..metrics.progression import checkProgressionMetrics
from ..metrics.validation import checkValidationMetrics
from ..termination.earlyTermination import _check_et_list
from ..utils.random import get_random_state
from .results import EnsemblePartialResult


class _ProgressiveEnsembleKMeansInterface(ABC):
    @validate_params(
        {
            "data": [str, "array-like", "sparse matrix"],
            "n_clusters": [Interval(Integral, 1, None, closed="left")],
            "n_runs": [Interval(Integral, 1, None, closed="left")],
            "random_state": ["random_state"],
            "freq": [None, Interval(Real, 0, None, closed="left")],
            "adjustCentroids": [bool],
            "adjustLabels": [bool],
        },
        prefer_skip_nested_validation=True,
    )
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
        taskId=None,
        **kwargs,
    ):

        if data is None:
            raise ValueError("Parameter 'data' must not be None.")

        # self._id = kwargs["id"] if "id" in kwargs else str(uuid.uuid4())
        self._id = taskId if taskId is not None else str(uuid.uuid4())
        self._data = data
        self._n_clusters = n_clusters
        self._n_runs = n_runs
        self._init = _check_init(init, n_runs)
        self._max_iter = _check_max_iter(max_iter, n_runs)
        self._tol = _check_tol(tol, n_runs)
        self._random_state = get_random_state(random_state)
        self._freq = freq

        self._ets = _check_et_list(ets)

        self._labelsValidationMetrics = checkValidationMetrics(labelsValidationMetrics)
        self._labelsComparisonMetrics = checkComparisonMetrics(labelsComparisonMetrics)
        self._labelsProgressionMetrics = checkProgressionMetrics(labelsProgressionMetrics)

        self._partitionsValidationMetrics = checkValidationMetrics(partitionsValidationMetrics)
        self._partitionsComparisonMetrics = checkComparisonMetrics(partitionsComparisonMetrics)
        self._partitionsProgressionMetrics = checkProgressionMetrics(partitionsProgressionMetrics)

        self._adjustCentroids = adjustCentroids
        self._adjustLabels = adjustLabels
        self._returnPartitions = returnPartitions
        self._taskId = taskId

    @abstractmethod
    def hasNextIteration(self) -> bool:
        pass

    @abstractmethod
    def executeNextIteration(self) -> EnsemblePartialResult:
        pass

    @abstractmethod
    def executeAllIterations(self) -> EnsemblePartialResult:
        pass

    @abstractmethod
    def kill(self):
        pass

    @abstractmethod
    def killRun(self, run):
        pass


########################################################################################################################
########################################################################################################################
########################################################################################################################


def _check_init(init_value, n_runs):
    """
    Validate the 'init' parameter for clustering initialization.

    Parameters:
    - init_value (str or list): The initialization method or a list of initialization methods.
        If a string, it must be either 'random' or 'k-means++'.
        If a list, it should contain strings, and all elements must be either 'random' or 'k-means++'.
    - n_runs (int): The number of runs.

    Returns:
    - list: A list of valid initialization methods, one for each run.

    Raises:
    - ValueError: If the 'init' parameter is not provided or has an invalid value.
                  If 'init' is a string and not 'random' or 'k-means++'.
                  If 'init' is a list and has an incorrect length or contains values other than 'random' or 'k-means++'.

    Example:
    >>> _check_init(init='random', n_runs=3)
    ['random', 'random', 'random']

    >>> _check_init(init=['random', 'k-means++', 'random'], n_runs=3)
    ['random', 'k-means++', 'random']

    >>> _check_init(init=['random', 'invalid_value'], n_runs=2)
    Traceback (most recent call last):
      ...
    ValueError: Invalid values in the 'init' list. All elements must be either 'random' or 'k-means++'.

    >>> _check_init(init='invalid_value', n_runs=2)
    Traceback (most recent call last):
      ...
    ValueError: Invalid value for 'init'. It must be either 'random' or 'k-means++'.
    """
    if init_value is None:
        raise ValueError("Parameter 'init' is required.")

    if isinstance(init_value, str):
        if init_value not in ["random", "k-means++"]:
            raise ValueError("Invalid value for 'init'. It must be either 'random' or 'k-means++'.")
        else:
            return [init_value for _ in range(n_runs)]
    elif isinstance(init_value, list):
        if len(init_value) != n_runs:
            raise ValueError(f"Invalid length for the 'init' list. The correct length must be {n_runs}.")
        if not all(element in ["random", "k-means++"] for element in init_value):
            raise ValueError("Invalid values in the 'init' list. All elements must be either 'random' or 'k-means++'.")
        return init_value
    else:
        raise ValueError("Invalid type for 'init'. It must be a string or a list of strings.")


def _check_max_iter(max_iter, n_runs):
    """
    Check the validity of the 'max_iter' parameter.

    Parameters:
    - max_iter (int or list): The maximum number of iterations for convergence.
        If an int, it must be >= 1.
        If a list, it should contain integers, and all elements must be >= 1 and have a length equal to 'n_runs'.
    - n_runs (int): The number of runs.

    Returns:
    - list: A list of 'max_iter' values, one for each run.

    Raises:
    - ValueError: If 'max_iter' is not provided or has an invalid value.
                  If 'max_iter' is an int and not >= 1.
                  If 'max_iter' is a list and has an incorrect length or contains values < 1.

    Example:
    >>> _check_max_iter(max_iter=300, n_runs=3)
    [10, 10, 10]

    >>> _check_max_iter(max_iter=[5, 8, 12], n_runs=3)
    [5, 8, 12]

    >>> _check_max_iter(max_iter=0, n_runs=2)
    Traceback (most recent call last):
      ...
    ValueError: Invalid value for 'max_iter'. It must be an integer >= 1.

    >>> _check_max_iter(max_iter=[3, -1], n_runs=2)
    Traceback (most recent call last):
      ...
    ValueError: Invalid values in the 'max_iter' list. All elements must be integers >= 1.
    """
    if max_iter is None:
        raise ValueError("Parameter 'max_iter' is required.")

    if isinstance(max_iter, int):
        if max_iter < 1:
            raise ValueError("Invalid value for 'max_iter'. It must be an integer >= 1.")
        return [max_iter for _ in range(n_runs)]
    elif isinstance(max_iter, list):
        if len(max_iter) != n_runs:
            raise ValueError(
                f"Invalid length for the 'max_iter' list. It must have a length equal to 'n_clusters' ({n_runs})."
            )
        if not all(isinstance(val, int) and val >= 1 for val in max_iter):
            raise ValueError("Invalid values in the 'max_iter' list. All elements must be integers >= 1.")
        return max_iter
    else:
        raise ValueError("Invalid type for 'max_iter'. It must be an integer or a list of integers.")


def _check_tol(tol, n_runs):
    """
    Validate the 'tol' parameter for clustering algorithms.

    Parameters:
    - tol (float or list): The tolerance value for convergence.
        If a float, it must be >= 0.
        If a list, it should contain floats, and all elements must be >= 0 and have a length equal to 'n_runs'.
    - n_runs (int): The number of runs.

    Returns:
    - list: A list of 'tol' values, one for each run.

    Raises:
    - ValueError: If 'tol' is not provided or has an invalid value.
                  If 'tol' is a float and not >= 0.
                  If 'tol' is a list and has an incorrect length or contains values < 0.

    Example:
    >>> _check_tol(tol=0.001, n_runs=3)
    [0.001, 0.001, 0.001]

    >>> _check_tol(tol=[0.005, 0.01, 0.002], n_runs=3)
    [0.005, 0.01, 0.002]

    >>> _check_tol(tol=-0.01, n_runs=2)
    Traceback (most recent call last):
      ...
    ValueError: Invalid value for 'tol'. It must be a float >= 0.

    >>> _check_tol(tol=[0.003, -0.005], n_runs=2)
    Traceback (most recent call last):
      ...
    ValueError: Invalid values in the 'tol' list. All elements must be floats >= 0.
    """
    if tol is None:
        raise ValueError("Parameter 'tol' is required.")

    if isinstance(tol, float):
        if tol < 0:
            raise ValueError("Invalid value for 'tol'. It must be a float >= 0.")
        return [tol for _ in range(n_runs)]
    elif isinstance(tol, list):
        if len(tol) != n_runs:
            raise ValueError(
                f"Invalid length for the 'tol' list. It must have a length equal to 'n_clusters' ({n_runs})."
            )
        if not all(isinstance(val, (int, float)) and val >= 0 for val in tol):
            raise ValueError("Invalid values in the 'tol' list. All elements must be floats >= 0.")
        return tol
    else:
        raise ValueError("Invalid type for 'tol'. It must be a float or a list of floats.")
