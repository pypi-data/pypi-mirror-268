import numpy as np
import sklearn.metrics as _skmetrics

# from sklearn.metrics import a
from sklearn.utils._param_validation import InvalidParameterError


def ari(labels_a, labels_b):
    """Rand index adjusted for chance.
    See https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_rand_score.html"""
    return _skmetrics.adjusted_rand_score(np.asarray(labels_a, dtype=int), np.asarray(labels_b, dtype=int))


def ami(labels_a, labels_b):
    """Adjusted Mutual Information between two clusterings.
    See https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_mutual_info_score.html"""
    return _skmetrics.adjusted_mutual_info_score(np.asarray(labels_a, dtype=int), np.asarray(labels_b, dtype=int))


ALL_COMPARISON_METRICS_DICT = {"ari": ari, "ami": ami}
ALL_COMPARISON_METRICS = sorted(ALL_COMPARISON_METRICS_DICT.keys())


def checkComparisonMetrics(names):
    """
    Check and validate the input comparison metric names.

    Parameters:
    - names (str, list, or None): The comparison metric name(s) to be checked.
        If None, an empty list is returned.
        If "ALL", returns a list of all available comparison metric names.
        If a list, checks each metric name and returns a list of valid metric names.

    Returns:
    - list: A list of valid comparison metric names.

    Raises:
    - InvalidParameterError: If the 'names' parameter is invalid.
        If a metric name in the list does not exist in the predefined metrics.
        If the 'names' parameter is not None, "ALL", or a list.

    Example:
    >>> checkComparisonMetrics("ALL")
    ['ari', 'ami', ...]

    >>> checkComparisonMetrics(["ari", "ami"])
    ['ari', 'ami']

    >>> checkComparisonMetrics("invalid_metric")
    Traceback (most recent call last):
      ...
    InvalidParameterError: The comparison 'invalid_metric' metric does not exist.

    >>> checkComparisonMetrics(["ari", "invalid_metric"])
    Traceback (most recent call last):
      ...
    InvalidParameterError: The comparison metric 'invalid_metric' does not exist.
    """
    if names is None:
        return []
    elif names == "ALL":
        return list(ALL_COMPARISON_METRICS_DICT.keys())
    elif isinstance(names, list):
        result = []
        for n in names:
            if n in ALL_COMPARISON_METRICS_DICT:
                result.append(n)
            else:
                raise InvalidParameterError(f"The comparison metric '{n}' does not exist.")
        return result
    else:
        raise InvalidParameterError(
            f"The 'names' parameter is invalid. It can be a single string or list of valid metric names."
            f"\nAvailable metrics are {list(ALL_COMPARISON_METRICS_DICT.keys())}."
            f"\nPass 'ALL' as a shortcut for all the metrics."
        )


def getComparisonMetricFunctionByName(name):
    """
    Retrieve a comparison metric function by its name.

    Parameters:
    - name (str): The name of the comparison metric function to be retrieved.

    Returns:
    - function: The comparison metric function corresponding to the provided name.

    Raises:
    - InvalidParameterError: If the provided 'name' does not exist in the predefined metrics.

    Example:
    >>> getComparisonMetricFunctionByName("ari")
    <function metric1 at 0x...>

    >>> getComparisonMetricFunctionByName("invalid_metric")
    Raises InvalidParameterError: The comparison metric 'invalid_metric' does not exist.
    """
    if name not in ALL_COMPARISON_METRICS_DICT:
        raise InvalidParameterError(f"The comparison metric '{name}' does not exist.")
    return ALL_COMPARISON_METRICS_DICT[name]


__all__ = [
    "checkComparisonMetrics",
    "getComparisonMetricFunctionByName",
    "ALL_COMPARISON_METRICS",
    "ALL_COMPARISON_METRICS_DICT",
    "ari",
    "ami",
]
