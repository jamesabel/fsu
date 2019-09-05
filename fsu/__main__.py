import os
import argparse

from fsu import __application_name__, longest_path, longest_path_command


def fsu():
    parser = argparse.ArgumentParser(prog=__application_name__)
    parser.add_argument("-c", "--command", required=True, help="commands: {longest_path_command}")
    parser.add_argument("-p", "--path", help="path")
    args = parser.parse_args()

    if args.command == longest_path_command:
        lp = longest_path(args.path)
        for p in [lp, os.path.abspath(lp)]:
            print(f"{p} ({len(p)})")
    else:
        print(f"{args.command} is not a valid command (use -h for help)")


if __name__ == "__main__":
    fsu()
