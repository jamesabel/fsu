
import os
from glob import glob

longest_path_command = "lp"


def longest_path(parent_path: str) -> str:
    max_path = None
    for p in glob(os.path.join(parent_path, "**", "*"), recursive=True):
        if max_path is None or len(p) > len(max_path):
            max_path = p
    return max_path
