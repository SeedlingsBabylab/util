import pandas as pd

its_times = pd.read_csv("../videotimes/videotimes.csv")

prefixes = its_times.file.str[:5].values

subjects = []
months = []

all_prefixes = []

for x in prefixes:
    x = x[:5]
    split = x.split("_")
    subjects.append(split[0])
    months.append(split[1])

subjects = set(subjects)
months = set(months)

for subject in subjects:
    for month in months:
        all_prefixes.append("{}_{}".format(subject, month))

result = pd.DataFrame(all_prefixes, columns=["file"])

result.to_csv("all_files_videotimes.csv", index=False)


all_prefixes = set(all_prefixes)

print(len(all_prefixes))
print(len(prefixes))
missing = all_prefixes - set(prefixes)
missing = pd.DataFrame(list(missing), columns=["file"])
missing.to_csv("missing_files_videotimes.csv", index=False)
print
