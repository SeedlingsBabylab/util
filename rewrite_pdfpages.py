import csv
import sys




if __name__ == "__main__":

    ocr_file = sys.argv[1]

    with open(ocr_file, "rU") as input:
        reader = csv.reader(input)
        header = reader.next()
        with open("output.csv", "wb") as output:
            writer = csv.writer(output)
            writer.writerow(header)
            for row in reader:
                row[1] = int(row[1]) - 529
                writer.writerow(row)
