import sys
import pandas as pd

if __name__ == "__main__":

    input_f = sys.argv[1]

    its_times = pd.read_csv(input_f)

    prefixes = its_times.file.str[:5].values

    subjects = []
    months = []

    all_prefixes = []

    for x in prefixes:
        split = x.split("_")
        subjects.append(split[0])
        months.append(split[1])

    subjects = set(subjects)
    months = set(months)

    for subject in subjects:
        for month in months:
            all_prefixes.append("{}_{}".format(subject, month))

    result = pd.DataFrame(all_prefixes, columns=["file"])

    result.to_csv("all_files.csv", index=False)

    all_prefixes = set(all_prefixes)
    missing = all_prefixes - set(prefixes)
    missing = pd.DataFrame(list(missing), columns=["file"])
    missing.to_csv("missing_files.csv", index=False)
    print
