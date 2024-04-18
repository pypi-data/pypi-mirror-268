import argparse
import json

from .importer import DatasetsImporter
from .loader import DatasetLoader


def _list():
    result = DatasetLoader.allNamesImported()
    print(f"Found {len(result)} imported datasets:")
    if len(result) > 0:
        print(json.dumps(result, indent=2))

    result = DatasetLoader.allNamesInPackage()
    print(f"\nFound {len(result)} datasets in the package:")
    if len(result) > 0:
        print(json.dumps(result, indent=2))


def _dlist():
    result = DatasetsImporter.listDownloadableDatasets()
    print(f"Found {len(result)} downloadable datasets:")
    for i, d in enumerate(result):
        print(f"\t{i+1}) {d}")


def _import(
    inputFilePath,
    sampleSizePercent=None,
    sampleRandomState=None,
    computeAllProjections=False,
    computeIsomap=False,
    computeMds=False,
    computePca=False,
    computeTsne=False,
    computeUmap=False,
):
    DatasetsImporter.importDataset(
        inputFilePath,
        sampleSizePercent=sampleSizePercent,
        sampleRandomState=sampleRandomState,
        computeAllProjections=computeAllProjections,
        computeIsomap=computeIsomap,
        computeMds=computeMds,
        computePca=computePca,
        computeTsne=computeTsne,
        computeUmap=computeUmap,
    )


def _download(nameOrNumber):
    DatasetsImporter.download(nameOrNumber)


def _delete(name):
    DatasetsImporter.deleteImportedDataset(name)


def main(args):
    if args.command == "list":
        _list()
    elif args.command == "import":
        _import(
            args.file,
            sampleSizePercent=args.sampleSizePercent,
            sampleRandomState=args.sampleRandomState,
            computeAllProjections=args.ap,
            computeIsomap=args.isomap,
            computeMds=args.mds,
            computePca=args.pca,
            computeTsne=args.tsne,
            computeUmap=args.umap,
        )
    elif args.command == "download":
        _download(args.nameOrNumber)
    elif args.command == "remove":
        _delete(args.name)
    elif args.command == "dlist":
        _dlist()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="pek.data")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # list
    p_list = subparsers.add_parser("list", help="List the imported datasets")

    # dlist
    p_dlist = subparsers.add_parser("dlist", help="List the downloadable datasets")

    # import <file>
    p_import = subparsers.add_parser("import", help="Import a dataset")
    p_import.add_argument("file", help="dataset file or folder in which to search for csv")

    # download <nameOrNumber>
    p_download = subparsers.add_parser("download", help="Download a dataset")
    p_download.add_argument("nameOrNumber", help="name or number of the dataset to download")

    # projections
    p_import.add_argument(
        "-ap",
        "--ap",
        help="Tells whether compute all projections (PCA, TSNE, UMAP) projection",
        action="store_true",
        default=False,
    )

    p_import.add_argument("-isomap", "--isomap", help="Tells whether compute ISOMAP projection", action="store_true")
    p_import.add_argument("-mds", "--mds", help="Tells whether compute MDS projection", action="store_true")
    p_import.add_argument("-pca", "--pca", help="Tells whether compute PCA projection", action="store_true")
    p_import.add_argument("-tsne", "--tsne", help="Tells whether compute TSNE projection", action="store_true")
    p_import.add_argument("-umap", "--umap", help="Tells whether compute UMAP projection", action="store_true")

    # sampling
    p_import.add_argument(
        "-sampleSizePercent",
        "--sampleSizePercent",
        help="Tells whether extract a sample from the dataset. Only integer from 1 to 100.",
        default=None,
    )
    p_import.add_argument(
        "-sampleRandomState", "--sampleRandomState", help="Random state for sampling. Integer.", default=None
    )

    # delete <name>
    p_remove = subparsers.add_parser("delete", help="delete an imported a dataset")
    p_remove.add_argument("name", help="dataset name")

    main(parser.parse_args())
