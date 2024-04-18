import numpy as np
from sklearn.metrics.pairwise import euclidean_distances


def getClusters(data, labels):
    """
    Returns a tuple (clusters, centers). If we have k clusters:
    - clusters: an array [c_1, ..., c_k] where c_i is the cluster i as ndarray (subset of data).
    - centers: an array [c_1, ..., c_k] where ci is the center of the cluster i.
    """
    unique_labels = np.unique(labels)
    clusters_idx = [np.where(labels == l) for l in unique_labels]
    clusters = [data[i] for i in clusters_idx]
    centers = np.array([np.mean(c, axis=0) for c in clusters], dtype=float)
    return clusters, centers


"""def best_labels_dtype(n_clusters):
    #Best dtype for the number of distinct label existing
    if n_clusters <= 255:
        return np.uint8
    elif n_clusters <= 65535:
        return np.uint16
    else:
        return np.uint32"""


def adjustLabels_fn(currLabels, currCentroids, prevCentroids):
    """Adjust labels in order to be robust again permutation of labels with the same clustering.
    Looks to the previous centroids to maintain consistence."""
    dist = euclidean_distances(currCentroids, prevCentroids)

    mapping = [None for _ in range(dist.shape[0])]
    while mapping.count(None) != 0:
        i, j = np.unravel_index(dist.argmin(), dist.shape)  # index of min value of distance
        dist[i] = np.inf  # remove row i from matrix (set distance to infinite)
        dist[:, j] = np.inf  # remove row j from matrix (set distance to infinite)
        mapping[i] = j  # currCentroids[i] is mapped to prevCentroids[j] --> label i is mapped to j

    adjustedLabels = currLabels.copy()
    for i, j in enumerate(mapping):
        # label i is mapped to j
        adjustedLabels[currLabels == i] = j

    return adjustedLabels


def adjustCentroids_fn(runs):
    """Adjust initial centroids to minimize difference of labeling among runs.
    The first centroid of run1 must be the closest centroid to the first centroid of run0.
    Run0 is the one that guides the assignments. Complexity: r^2 * k"""
    A = runs[0]._centers  # centroids of run[0]
    B = [
        runs[j]._centers for j in range(1, len(runs))
    ]  # list of centroids for each remaining run. B[j] = centroids of run [j+1]

    assigned = [[None for z in range(len(A))] for j in range(len(B))]

    for i in range(len(A)):
        for j in range(len(B)):
            dist = euclidean_distances(
                B[j], [A[i]]
            ).flatten()  # distances for each centroids in B[j] to centroid A[i], array 1D
            candidates = np.argsort(dist)
            for z in candidates:
                if assigned[j][z] is None:
                    assigned[j][z] = i
                    break

    for j in range(len(B)):
        newCenters = np.empty_like(B[j])
        for z in range(len(newCenters)):
            t = assigned[j][z]
            newCenters[z] = B[j][t]

        i = j + 1
        runs[i]._centers = newCenters
