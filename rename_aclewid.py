import sys
import os
import shutil

import pandas as pd


def rename(df, input):
    rename_list = pd.DataFrame(columns=["orig_name", "new_name"])
    for root, dirs, files in os.walk(input):
        for file in files:
            if not file.startswith("."):
                prefix = file[:5]
                rec = df.query(
                    "(lab_internal_subject_id == \"{}\") and (corpus == \"Seedlings\")".format(prefix))
                aid = rec.iloc[0].aclew_id
                print "{} -- {}".format(prefix, aid)

                newname = "{}{}".format(aid, os.path.splitext(file)[1])
                # newname = file.replace(prefix, aid)
                rename_list = rename_list.append(
                    {"orig_name": file, "new_name": newname}, ignore_index=True)
                os.rename(os.path.join(root, file),
                          os.path.join(root, newname))
    return rename_list


if __name__ == "__main__":

    aclew_df = pd.read_csv(sys.argv[1], dtype={'aclew_id': str})
    input_dir = sys.argv[2]

    name_list = rename(aclew_df, input_dir)

    name_list.to_csv("renamed_files.csv", index=False)
