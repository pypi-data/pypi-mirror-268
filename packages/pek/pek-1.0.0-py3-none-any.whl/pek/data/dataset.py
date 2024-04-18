import json

import numpy as np
from sklearn.utils import Bunch

from ..utils.encoding import NumpyEncoder


def _read(hdf5File, attr, dtype=np.float64):
    if attr not in hdf5File:
        return None
    else:
        return np.array(hdf5File[attr], dtype=dtype)


class Dataset:
    def __init__(self, name, hdf5File):
        self._name = name
        self._hdf5File = hdf5File

        self._features = None
        self._data = None
        self._datasc = None
        self._isomap = None
        self._mds = None
        self._pca = None
        self._tsne = None
        self._umap = None

    def toDict(self, insertData=True, insertProjections=True):
        d = Bunch(
            name=self.name,
            features=self.features,
        )

        if insertData:
            d["data"] = self.data

        if insertProjections:
            d["projections"] = Bunch(isomap=self.isomap, mds=self.mds, pca=self.pca, tsne=self.tsne, umap=self.umap)

        return d

    def toJson(self, insertData=True, insertProjections=True, indent=None):
        return json.dumps(
            self.toDict(insertData=insertData, insertProjections=insertProjections), cls=NumpyEncoder, indent=indent
        )

    @property
    def name(self):
        return self._name

    @property
    def features(self):
        if self._features is None:
            self._features = _read(self._hdf5File, "features", dtype=str)
        if self._features is None:
            self._features = _read(self._hdf5File, "header", dtype=str)
        return self._features

    @property
    def data(self):
        if self._data is None:
            self._data = _read(self._hdf5File, "data")
        return self._data

    @property
    def datasc(self):
        if self._datasc is None:
            self._datasc = _read(self._hdf5File, "datasc")
        return self._datasc

    @property
    def isomap(self):
        if self._isomap is None:
            self._isomap = _read(self._hdf5File, "isomap")
        return self._isomap

    @property
    def mds(self):
        if self._mds is None:
            self._mds = _read(self._hdf5File, "mds")
        return self._mds

    @property
    def pca(self):
        if self._pca is None:
            self._pca = _read(self._hdf5File, "pca")
        return self._pca

    @property
    def tsne(self):
        if self._tsne is None:
            self._tsne = _read(self._hdf5File, "tsne")
        return self._tsne

    @property
    def umap(self):
        if self._umap is None:
            self._umap = _read(self._hdf5File, "umap")
        return self._umap

    def getDataMatrix(self, t: str):
        if t == "data":
            return self.data
        elif t == "datasc":
            return self.datasc
        elif t == "isomap":
            return self.isomap
        elif t == "mds":
            return self.mds
        elif t == "pca":
            return self.pca
        elif t == "tsne":
            return self.tsne
        elif t == "umap":
            return self.umap
        else:
            raise ValueError(f"The type '{t}' of data matrix does not exist.")

    def __str__(self):
        return f"{self.__class__.__name__}<{self.name}> shape={self.data.shape}"
