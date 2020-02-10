import csv

with open('data7.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # skip first line
    next(csv_reader)

    for line in csv_reader:
        # print(line)
        print(line[1])
