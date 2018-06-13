import sys
import csv
import os

if __name__ == "__main__":
    start_dir = sys.argv[1]

    scrubbed = []

    for root, dirs, files in os.walk(start_dir):
        for file in files:
            if "scrubbed" in file:
                scrubbed.append(file)


    with open("results.csv", "wb") as output:
        writer = csv.writer(output)
        for file in scrubbed:
            writer.writerow([file])
