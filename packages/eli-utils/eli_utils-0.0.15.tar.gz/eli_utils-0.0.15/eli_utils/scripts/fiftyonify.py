import argparse
from ..plotting import view_in_fiftyone


def parse_args():
    parser = argparse.ArgumentParser(description="View data in FiftyOne")
    parser.add_argument("paths", metavar="paths", type=str, nargs="+", help="List of paths to view")
    parser.add_argument(
        "--jsons",
        metavar="jsons",
        type=str,
        nargs="+",
        help="List of JSON paths or dictionaries",
        default=None,
    )
    parser.add_argument("--dataset", type=str, default="tmp", help="Name of the dataset")
    parser.add_argument(
        "--persistent", action="store_true", help="Flag to keep the session persistent"
    )
    parser.add_argument(
        "--address",
        type=str,
        default="0.0.0.0",
        help="IP address to bind the server to",
    )
    parser.add_argument("--port", type=int, help="Port number for the server")
    parser.add_argument(
        "--wait",
        action="store_true",
        help="Flag to wait for the server to start before returning",
    )

    args = parser.parse_args()
    return args


def main():
    args = parse_args()

    paths = args.paths
    jsons = args.jsons
    dataset = args.dataset
    persistent = args.persistent
    address = args.address
    port = args.port
    wait = args.wait

    view_in_fiftyone(
        paths=paths,
        jsons=jsons,
        dataset=dataset,
        persistent=persistent,
        address=address,
        port=port,
        wait=wait,
    )

if __name__ == "__main__":
    main()
