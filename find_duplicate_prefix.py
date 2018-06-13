import sys
import os

from collections import Counter

if __name__ == "__main__":

    start_dir = sys.argv[1]

    files = [file[0:5] for file in os.listdir(start_dir)]

    counted_files = Counter(files)

    with open("duplicate_files.csv", "wb") as output:
        for key, value in counted_files.iteritems():
            if value != 1:
                output.write("{}\n".format(key))

    # for thing in counted_files.values:
    #     print thing

    print len(counted_files)
