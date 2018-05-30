import sys
import csv
import os


def walk_tree(start, out):
    for root, dirs, files in os.walk(start):
        for file in files:
            if file.endswith(".csv"):
                print file
                with open(os.path.join(root, file), "rU") as input:
                    with open(os.path.join(out, file), "wb") as output:
                        reader = csv.reader(input)
                        head = reader.next()
                        writer = csv.writer(output)
                        # determine if file is audio or video bl
                        if any("ordinal" in x for x in head):
                            print
                        else:
                            # if "01_17" in file:
                                if len(head) > 7:
                                    if head[-1] == "comment" or head[-1] == "":
                                        writer.writerow(head[:-1])
                                elif len(head) == 7:
                                    writer.writerow(head)
                                else:
                                    raise Exception(file)
                                for row in reader:
                                    if len(row) > 7:
                                        writer.writerow(row[:7])
                                    else:
                                        writer.writerow(row)


if __name__ == "__main__":
    start = sys.argv[1]
    out = sys.argv[2]

    walk_tree(start, out)
