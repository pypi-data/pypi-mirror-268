import numpy as np
from sklearn.decomposition import PCA
from sklearn.manifold import MDS, TSNE, Isomap
from sklearn.preprocessing import MinMaxScaler, StandardScaler


def _scaleProjection(proj, dtype=float):
    """Scale the features of a projection in [-1, 1]"""
    return np.asarray(MinMaxScaler((-1, 1)).fit_transform(proj), dtype=dtype, order="C")


def _compute(name, fn, dataScaled, dtype=float):
    print(f"\tComputing {name} ...")
    proj = dataScaled
    if dataScaled.shape[1] > 2:
        proj = fn.fit_transform(dataScaled)
    return _scaleProjection(proj, dtype)


class Projection:
    @staticmethod
    def computeISOMAP(dataScaled, dtype=float):
        fn = Isomap(n_components=2)
        return _compute("ISOMAP", fn, dataScaled, dtype=dtype)

    @staticmethod
    def computeMDS(dataScaled, dtype=float):
        fn = MDS(n_components=2, normalized_stress="auto", random_state=0)
        return _compute("MDS", fn, dataScaled, dtype=dtype)

    @staticmethod
    def computePCA(dataScaled, dtype=float):
        fn = PCA(n_components=2, random_state=0)
        return _compute("PCA", fn, dataScaled, dtype=dtype)

    @staticmethod
    def computeTSNE(dataScaled, dtype=float):
        fn = TSNE(n_components=2, random_state=0)
        return _compute("TSNE", fn, dataScaled, dtype=dtype)

    @staticmethod
    def computeUMAP(dataScaled, dtype=float):
        from umap import UMAP

        fn = UMAP()
        return _compute("UMAP", fn, dataScaled, dtype=dtype)
