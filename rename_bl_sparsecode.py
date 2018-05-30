import os
import sys
import shutil

if __name__ == "__main__":

    start_dir = sys.argv[1]
    out_dir = sys.argv[2]
    for root, dirs, files in os.walk(start_dir):
        for file in files:
            if file.endswith(".csv"):
                ftype = "audio" if "audio" in file else "video"
                shutil.copy(os.path.join(root, file),
                            os.path.join(out_dir, "{}_{}_sparse_code.csv".format(file[:5], ftype)))