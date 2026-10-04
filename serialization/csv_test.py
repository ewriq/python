import csv

with open("data.csv", "r+") as file_handle:
    reader = csv.reader(file_handle)
    writer = csv.writer(file_handle)
    for row in reader:
        print(row)
    writer.writerow(["ewriq1", 1])
    writer.writerow(["ewriq2", 2])
