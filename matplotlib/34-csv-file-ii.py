import csv

with open('data7.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('data7-copy.csv', 'w') as new_file:
        # csv_writer = csv.writer(new_file, delimiter='-')
        csv_writer = csv.writer(new_file, delimiter='\t')

        for line in csv_reader:
            csv_writer.writerow(line)
