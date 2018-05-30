import csv
import os

import sys


audio_file_dir = "../collect/all_cha"
video_csv_dir = "data/pho_csv_output"

# with open("collect_???_audio.csv", "wb") as out:
#     writer = csv.writer(out)
#     writer.writerow(["file", "line_num", "line"])
#     for root, dirs, files in os.walk(audio_file_dir):
#         for file in files:
#             if file.endswith(".cha"):
#                 with open(os.path.join(root, file), "rU") as input_f:
#                     for index, line in enumerate(input_f):
#                         if "???" in line:
#                             writer.writerow([file, index, line])

with open("collect_???_video.csv", "wb") as out:
    writer = csv.writer(out)
    writer.writerow(["file", "line"])
    for root, dirs, files in os.walk(video_csv_dir):
        for file in files:
            if file.endswith(".csv"):
                with open(os.path.join(root, file), "rU") as input_f:
                    reader = csv.reader(input_f)
                    reader.next()
                    for row in reader:
                        print row[3]
                        if "???" in row[3]:
                            writer.writerow([file, " ".join(row)])

                    