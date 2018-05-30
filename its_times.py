import xml.etree.ElementTree as ET
import sys
import os
import csv
import datetime as dt
import pandas as pd


def extract_recording_time(file):
    tree = ET.parse(file)
    result = tree.find("ProcessingUnit/UPL_SectorSummary/Item")
    return dt.datetime.strptime(result.attrib["timeStamp"], "%Y-%m-%dT%H:%M:%SZ")


if __name__ == "__main__":
    input_dir = sys.argv[1]
    results = []

    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith(".its"):
                print file
                t = extract_recording_time(os.path.join(root, file))
                results.append((file[:5], t.isoformat()))

    df = pd.DataFrame(results, columns=["file", "time"])
    df = df.sort_values(by="file")
    df.to_csv("its_times.csv", index=False)
