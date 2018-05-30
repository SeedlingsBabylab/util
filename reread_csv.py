import csv
import sys

if __name__ == "__main__":
    input_csv = sys.argv[1]
    output_csv = sys.argv[2]


    with open(input_csv, "rU") as inputf:
        with open(output_csv, "wb") as outf:
            reader = csv.reader(inputf)
            writer = csv.writer(outf)
            for row in reader:
                writer.writerow(row)


                