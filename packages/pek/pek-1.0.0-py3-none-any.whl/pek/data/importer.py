import os
from abc import ABC
from pathlib import Path

import h5py
import numpy as np
import pandas as pd
import requests
from downloader_cli.download import Download
from sklearn.preprocessing import StandardScaler

from ..version import __version__
from .folders import Folders
from .projection import Projection

_dtype_str = h5py.special_dtype(vlen=str)
_FLOAT = np.float32
_COMPRESSION = 9


def _readJsonFromUrl(inputFileUrl):
    """Loads a json from an url."""
    try:
        response = requests.get(inputFileUrl)
        response.raise_for_status()
        obj = response.json()
        return obj
    except Exception as err:
        print(f"An error occurred: {err}")
        raise err


class _Colors:
    ENDC = "\033[0m"
    GRAY = "\033[90m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    PINK = "\033[95m"


def _computeScaledData(data, dtype=float):
    print(f"\tScaling data ...")
    dataScaled = np.asarray(StandardScaler().fit_transform(data), dtype=dtype, order="C")
    return dataScaled


def _getDatasetFile(name):
    return Folders.importedDatasetsFolder().joinpath(f"{name}.hdf5")


class DatasetsImporter(ABC):
    @staticmethod
    def deleteImportedDataset(name):
        print(f"Deleting {name} ...")
        file = _getDatasetFile(name)
        if file.exists():
            os.remove(file)
        else:
            raise NameError(f"The dataset '{name}' is not an imported dataset.")

    @staticmethod
    def importDataset(
        inputFilePath,
        sampleSizePercent=None,
        sampleRandomState=None,
        computeAllProjections=False,
        computeIsomap=False,
        computeMds=False,
        computePca=True,
        computeTsne=False,
        computeUmap=False,
        **kwargs,
    ):

        toImport = []
        inputFilePath = Path(inputFilePath)
        if inputFilePath.is_dir():
            for f in inputFilePath.glob("*.csv"):
                toImport.append(f)
        else:
            toImport.append(inputFilePath)

        print(f"Found {len(toImport)} csv to import.")
        for f in toImport:
            DatasetsImporter._importCsvDataset(
                f,
                sampleSizePercent=sampleSizePercent,
                sampleRandomState=sampleRandomState,
                computeAllProjections=computeAllProjections,
                computeIsomap=computeIsomap,
                computeMds=computeMds,
                computePca=computePca,
                computeTsne=computeTsne,
                computeUmap=computeUmap,
                **kwargs,
            )

    @staticmethod
    def _importCsvDataset(
        inputFilePath,
        local=False,
        sampleSizePercent=None,
        sampleRandomState=None,
        computeAllProjections=False,
        computeIsomap=False,
        computeMds=False,
        computePca=True,
        computeTsne=False,
        computeUmap=False,
        **kwargs,
    ) -> Path:
        """Import a csv dataset."""
        inputFilePath = Path(inputFilePath)
        datasetName = inputFilePath.stem
        outputFilePath = _getDatasetFile(datasetName)

        if not inputFilePath.exists():
            raise RuntimeError(f"The file {inputFilePath.resolve()} does not exist.")

        if sampleSizePercent is not None:
            if int(sampleSizePercent) <= 0 or int(sampleSizePercent) > 100:
                raise RuntimeError(f"Invalid sample size percent {sampleSizePercent}.")

        if computeAllProjections or computeUmap:
            try:
                from umap import UMAP
            except ImportError:
                print(f"{_Colors.RED}ERROR: To compute UMAP you need to install the umap-learn package.{_Colors.ENDC}")
                print("See details at: https://pypi.org/project/umap-learn/")
                exit()

        print(f"Importing {inputFilePath.stem} ...")
        # create HDF5 file

        with h5py.File(outputFilePath, "w") as hf:
            info = hf.create_dataset("__info__", data=np.zeros(1), compression=_COMPRESSION)
            info.attrs["__version__"] = __version__
            if sampleSizePercent is not None:
                info.attrs["sampleSize"] = sampleSizePercent
                info.attrs["sampleRandomState"] = int(sampleRandomState)

            print(f"\tLoading input file ...")
            df = pd.read_csv(inputFilePath)

            # features
            features = np.asarray(list(df.columns), dtype=_dtype_str, order="C")
            hf.create_dataset("features", data=features, compression=_COMPRESSION)

            # data
            data = np.asarray(df.to_numpy(dtype=_FLOAT), order="C")

            if sampleSizePercent is not None:
                totLen = data.shape[0]
                sampledLen = int(np.ceil(totLen * float(sampleSizePercent) / 100))
                print(f"\tSampling to {sampledLen} entries...")
                data = np.random.default_rng(int(sampleRandomState)).choice(data, sampledLen, replace=False)

            hf.create_dataset("data", data=data, compression=_COMPRESSION)

            # scaled data with StandardScaler
            dataScaled = _computeScaledData(data, dtype=_FLOAT)
            hf.create_dataset("datasc", data=dataScaled, compression=_COMPRESSION)

            # projections
            if computeAllProjections or computeIsomap:
                _proj = Projection.computeISOMAP(dataScaled, dtype=_FLOAT)
                hf.create_dataset("isomap", data=_proj, compression=_COMPRESSION)

            if computeAllProjections or computeMds:
                _proj = Projection.computeMDS(dataScaled, dtype=_FLOAT)
                hf.create_dataset("mds", data=_proj, compression=_COMPRESSION)

            if computeAllProjections or computePca:
                _proj = Projection.computePCA(dataScaled, dtype=_FLOAT)
                hf.create_dataset("pca", data=_proj, compression=_COMPRESSION)

            if computeAllProjections or computeTsne:
                _proj = Projection.computeTSNE(dataScaled, dtype=_FLOAT)
                hf.create_dataset("tsne", data=_proj, compression=_COMPRESSION)

            if computeAllProjections or computeUmap:
                _proj = Projection.computeUMAP(dataScaled, dtype=_FLOAT)
                hf.create_dataset("umap", data=_proj, compression=_COMPRESSION)

            hf.flush()
            hf.close()

        return outputFilePath

    @staticmethod
    def listDownloadableDatasets():
        url = "https://raw.githubusercontent.com/aware-diag-sapienza/pekdata/main/index.json"
        index = _readJsonFromUrl(url)
        return index

    @staticmethod
    def download(nameOrNumber):
        available = DatasetsImporter.listDownloadableDatasets()

        name = None
        try:
            number = int(nameOrNumber) - 1
            name = available[number]
        except Exception as e:
            print(e)
            name = nameOrNumber

        if name not in available:
            raise ValueError(f"The '{name}' dataset does not exist. Avaliable datasets are: {available}")

        url = f"https://github.com/aware-diag-sapienza/pekdata/raw/main/data/{name}.hdf5"
        outFile = _getDatasetFile(name)
        Download(url, des=outFile).download()
