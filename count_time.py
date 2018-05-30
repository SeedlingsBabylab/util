import csv
import sys


if __name__ == "__main__":

    data = sys.argv[1]

    total_time = 0
    fanman_time = 0
    ids_time = 0
    ads_time = 0
    male_time = 0
    female_time = 0

    with open(data, "rU") as input:
        reader = csv.reader(input)
        reader.next()

        for row in reader:
            time_split = row[7].split("_")
            time_diff = int(time_split[1]) - int(time_split[0])
            total_time += time_diff
            if row[1]:
                fanman_time += time_diff
                if row[10] == "CDS":
                    ids_time += time_diff
                    # if row[11] == "MALE":
                    #     male_time += time_diff
                    # elif row[11] == "FEMALE":
                    #     female_time += time_diff
                elif row[10] == "ADS":
                    ads_time += time_diff
                    # if row[11] == "MALE":
                    #     male_time += time_diff
                    # elif row[11] == "FEMALE":
                    #     female_time += time_diff

                if row[11] == "MALE":
                    male_time += time_diff
                elif row[11] == "FEMALE":
                    female_time += time_diff
                else:
                    print "something's wrong: {}".format(row)


    print "total time: {}".format(total_time)
    print "fanman time: {}".format(fanman_time)
    print "ids time: {}".format(ids_time)
    print "ads time: {}".format(ads_time)
    print "male time: {}".format(male_time)
    print "female time: {}".format(female_time)
