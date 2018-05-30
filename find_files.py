import os
import sys

prefixes = ["31_08", "31_09", "33_08", "11_13"]
extensions = [".MTS", ".mts", ".mp4", ".MP4"]


def match(file):
    f, ext = os.path.splitext(file)
    if file[:5] in prefixes and ext in extensions:
        return True
    return False


if __name__ == "__main__":
    start = sys.argv[1]
    for root, dirs, files in os.walk(start):
        for file in files:
            if match(file):
                print os.path.join(root, file)
