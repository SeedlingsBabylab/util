import pandas as pd


all_bl = pd.read_csv("data/all_basiclevel.csv")


all_bl['proper'] = all_bl.basic_level.str[0:1].str.isupper()
print

all_bl.to_csv("all_basiclevel_with_proper.csv", index=False)


