import csv
import sys


def save_to_file(jobs):

    file = open("jobs.csv", "w", -1, "utf-8")
    writer = csv.writer(file)
    writer.writerow(["titile","company","location","link"])

    for job in jobs:
        writer.writerow(list(job.values()))
        # print(list(job.values()))

    return


