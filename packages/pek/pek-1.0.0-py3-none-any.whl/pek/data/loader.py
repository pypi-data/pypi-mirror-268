import pkgutil
from abc import ABC
from io import BytesIO

import h5py
import numpy as np

from .dataset import Dataset
from .folders import Folders


def _loadInPackageDataset(name):
    filePath = Folders.packageDataFolder() + f"{name}.hdf5"
    input = BytesIO(pkgutil.get_data(__name__, filePath))
    file = h5py.File(input, "r")
    return Dataset(name, file)


def _loadImportedDataset(name):
    """folder_local = Folders.importedDatasetsFolder(createIfNotExist=False)
    filePath = folder_local.joinpath(f"{name}.hdf5")
    if filePath.exists():
        file = h5py.File(filePath, "r")
        return Dataset(name, file)"""

    folder_home = Folders.importedDatasetsFolder(createIfNotExist=False)
    filePath = folder_home.joinpath(f"{name}.hdf5")
    if filePath.exists():
        file = h5py.File(filePath, "r")
        return Dataset(name, file)


class DatasetLoader(ABC):
    @staticmethod
    def allNamesInPackage():
        """List of all available datasets in the package."""
        ls = [
            "A1",
            "A2",
            "A3",
            "BalanceScale",
            "ContraceptiveMethodChoice",
            "Diabetes",
            "Glass",
            "HeartStatlog",
            "Ionosphere",
            "Iris",
            "LiverDisorder",
            "S1",
            "S2",
            "S3",
            "S4",
            "Segmentation",
            "Sonar",
            "SpectfHeart",
            "Unbalanced",
            "Vehicles",
            "Wine",
        ]
        return ls

    @staticmethod
    def allNamesImported():
        """List of all imported datasets."""
        result = set()

        """folder_local = Folders.importedDatasetsFolder(createIfNotExist=False)
        if folder_local.exists():
            for file in folder_local.glob(f"*.hdf5"):
                result.add(file.stem)"""

        folder_home = Folders.importedDatasetsFolder(createIfNotExist=False)
        if folder_home.exists():
            for file in folder_home.glob(f"*.hdf5"):
                result.add(file.stem)

        return sorted(list(result))

    @staticmethod
    def allNames() -> list:
        """Returns the list of all available dataset names."""
        ls = set()
        for d in DatasetLoader.allNamesInPackage():
            ls.add(d)
        for d in DatasetLoader.allNamesImported():
            ls.add(d)

        completeList = sorted(ls)
        return completeList

    @staticmethod
    def load(name) -> Dataset:
        """Loads a dataset given the name."""
        if name not in set(DatasetLoader.allNames()):
            raise ValueError(f"Dataset '{name}' does not exist.")

        if name in DatasetLoader.allNamesInPackage():
            return _loadInPackageDataset(name)
        elif name in DatasetLoader.allNamesImported():
            return _loadImportedDataset(name)
        else:
            raise ValueError(f"Dataset '{name}' does not exist.")

    @staticmethod
    def loadX(name) -> np.ndarray:
        """Loads the data matrix. Name can be the <datasetName> or <datasetName:dataMatrixType>."""
        if ":" in name:
            datasetName = name.split(":")[0]
            datasetMatrixType = name.split(":")[1]
            dataset = DatasetLoader.load(datasetName)
            X = dataset.getDataMatrix(datasetMatrixType)
            return X
        else:
            dataset = DatasetLoader.load(name)
            return dataset.data

    @staticmethod
    def loadAll() -> list:
        """Loads all the available datasets."""
        return [DatasetLoader.load(n) for n in DatasetLoader.allNames()]
