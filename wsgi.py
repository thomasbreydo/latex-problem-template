from argparse import ArgumentParser, Namespace

from app import app


def main():
    parser: ArgumentParser = ArgumentParser()
    parser.add_argument("--debug", help="Use Flask's DEBUG server", action="store_true")
    args: Namespace = parser.parse_args()
    app.debug = args.debug
    app.run()


if __name__ == "__main__":
    main()
