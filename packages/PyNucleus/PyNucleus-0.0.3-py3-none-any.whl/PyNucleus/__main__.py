import argparse

__version__ = "0.0.3"
__author__ = "Bartek Kansy"

def main():
    parser = argparse.ArgumentParser(description="Essential Python Toolkit.")
    parser.add_argument("--version", action="store_true", help="show package version")
    parser.add_argument("--author", action="store_true", help="show package author")
    args = parser.parse_args()

    if args.version:
        print("Version:", __version__)

    elif args.author:
        print("Author:", __author__)

if __name__ == "__main__":
    main()