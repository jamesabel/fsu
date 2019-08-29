
import os
import argparse

from fsu import __application_name__, longestpath


def fsu():
    parser = argparse.ArgumentParser(prog=__application_name__)
    parser.add_argument("-c", "--command", required=True, help="commands: longestpath")
    parser.add_argument("-p", "--path", help="path")
    args = parser.parse_args()

    if args.command == "longestpath":
        lp = longestpath(args.path)
        for p in [lp, os.path.abspath(lp)]:
            print(f'{p} ({len(p)})')
    else:
        print("no command given (use -h for help)")


if __name__ == "__main__":
    fsu()
