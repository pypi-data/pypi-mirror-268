import numpy as np
from sklearn.utils._param_validation import InvalidParameterError


def _entries_stability(labelsHistoryArr, window=None):
    """Stability of labels for each data entry,
    considering the array of labels of the iterations and the window (last elements). If none, consider all labels.."""

    if (window is not None) and (window < 2):
        raise InvalidParameterError(f"Parameter window must be >= 2. Got {window} instead.")

    if window is None:
        hist = labelsHistoryArr
    else:
        hist = labelsHistoryArr[-window:]

    if len(hist) == 1:
        return np.full_like(hist[0], 0, dtype=float)

    stability = np.full_like(hist[0], 0, dtype=float)
    h = len(hist)
    w = [np.log(2 + i) for i in range(h - 1)]  # log weights
    for i in range(h - 1):
        stability += ((hist[h - 1] == hist[i]).astype(float) * w[i]) / sum(w)
    return stability


def _global_stability(labelsHistory, window=None):
    """Mean stability of labels for all the data entries."""
    est = _entries_stability(labelsHistory, window)
    return float(np.mean(est))


########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################


def entries_stability_2(labelsHistoryArr):
    return _entries_stability(labelsHistoryArr, 2)


def entries_stability_3(labelsHistoryArr):
    return _entries_stability(labelsHistoryArr, 3)


def entries_stability_4(labelsHistoryArr):
    return _entries_stability(labelsHistoryArr, 3)


def entries_stability_5(labelsHistoryArr):
    return _entries_stability(labelsHistoryArr, 5)


def entries_stability_10(labelsHistoryArr):
    return _entries_stability(labelsHistoryArr, 10)


def entries_stability_all(labelsHistoryArr):
    return _entries_stability(labelsHistoryArr, None)


def global_stability_2(labelsHistoryArr):
    return _global_stability(labelsHistoryArr, 2)


def global_stability_3(labelsHistoryArr):
    return _global_stability(labelsHistoryArr, 3)


def global_stability_4(labelsHistoryArr):
    return _global_stability(labelsHistoryArr, 4)


def global_stability_5(labelsHistoryArr):
    return _global_stability(labelsHistoryArr, 5)


def global_stability_10(labelsHistoryArr):
    return _global_stability(labelsHistoryArr, 10)


def global_stability_all(labelsHistoryArr):
    return _global_stability(labelsHistoryArr, None)


ALL_PROGRESSION_METRICS_DICT = {
    "entries_stability_2": entries_stability_2,
    "entries_stability_3": entries_stability_3,
    "entries_stability_4": entries_stability_4,
    "entries_stability_5": entries_stability_5,
    "entries_stability_10": entries_stability_10,
    "entries_stability_all": entries_stability_all,
    "global_stability_2": global_stability_2,
    "global_stability_3": global_stability_3,
    "global_stability_4": global_stability_4,
    "global_stability_5": global_stability_5,
    "global_stability_10": global_stability_10,
    "global_stability_all": global_stability_all,
}
ALL_PROGRESSION_METRICS = sorted(ALL_PROGRESSION_METRICS_DICT.keys())


def checkProgressionMetrics(names):
    """
    Check and validate the input progression metric names.

    Parameters:
    - names (str, list, or None): The progression metric name(s) to be checked.
        If None, an empty list is returned.
        If "ALL", returns a list of all available progression metric names.
        If a list, checks each metric name and returns a list of valid metric names.

    Returns:
    - list: A list of valid progression metric names.

    Raises:
    - InvalidParameterError: If the 'names' parameter is invalid.
        If a metric name in the list does not exist in the predefined metrics.
        If the 'names' parameter is not None, "ALL", or a list.

    Example:
    >>> checkProgressionMetrics("ALL")
    ['calinski_harabasz', 'davies_bouldin', ...]

    >>> checkProgressionMetrics(["entries_stability_2", "global_stability_3"])
    ['entries_stability_2', 'global_stability_3']

    >>> checkProgressionMetrics("invalid_metric")
    Traceback (most recent call last):
      ...
    InvalidParameterError: The progression 'invalid_metric' metric does not exist.

    >>> checkProgressionMetrics(["entries_stability_2", "invalid_metric"])
    Traceback (most recent call last):
      ...
    InvalidParameterError: The progression metric 'invalid_metric' does not exist.
    """
    if names is None:
        return []
    elif names == "ALL":
        return list(ALL_PROGRESSION_METRICS_DICT.keys())
    elif isinstance(names, list):
        result = []
        for n in names:
            if n in ALL_PROGRESSION_METRICS_DICT:
                result.append(n)
            else:
                raise InvalidParameterError(f"The progression metric '{n}' does not exist.")
        return result
    else:
        raise InvalidParameterError(
            f"The 'names' parameter is invalid. It can be a single string or list of valid metric names."
            f"\nAvailable metrics are {list(ALL_PROGRESSION_METRICS_DICT.keys())}."
            f"\nPass 'ALL' as a shortcut for all the metrics."
        )


def getProgressionMetricFunctionByName(name):
    """
    Retrieve a progression metric function by its name.

    Parameters:
    - name (str): The name of the progression metric function to be retrieved.

    Returns:
    - function: The progression metric function corresponding to the provided name.

    Raises:
    - InvalidParameterError: If the provided 'name' does not exist in the predefined metrics.

    Example:
    >>> getProgressionMetricFunctionByName("entries_stability_2")
    <function metric1 at 0x...>

    >>> getProgressionMetricFunctionByName("invalid_metric")
    Raises InvalidParameterError: The progression metric 'invalid_metric' does not exist.
    """
    if name not in ALL_PROGRESSION_METRICS_DICT:
        raise InvalidParameterError(f"The progression metric '{name}' does not exist.")
    return ALL_PROGRESSION_METRICS_DICT[name]


__all__ = [
    "checkProgressionMetrics",
    "getProgressionMetricFunctionByName",
    "ALL_PROGRESSION_METRICS",
    "ALL_PROGRESSION_METRICS_DICT",
    "entries_stability_2",
    "entries_stability_3",
    "entries_stability_4",
    "entries_stability_5",
    "entries_stability_10",
    "entries_stability_all",
    "global_stability_2",
    "global_stability_3",
    "global_stability_4",
    "global_stability_5",
    "global_stability_10",
    "global_stability_all",
]
