import csv

with open('data7.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('data7-copy-dict.csv', 'w') as new_file:
        # fieldnames = ['first_name', 'last_name']
        fieldnames = ['first_name', 'last_name', 'email']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        # write keys
        csv_writer.writeheader()

        for line in csv_reader:
            # del line['email']
            csv_writer.writerow(line)

# Lines 7 and 16 work together to delete one key and all the associated to it.
