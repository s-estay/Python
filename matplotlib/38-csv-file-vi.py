import csv

# write mode
with open('log4.csv', 'w') as new_file:
    fieldnames = ['date', 'time', 'voltage', 'current', 'temperature']
    csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
    csv_writer.writeheader()

date = ['2020-01-28']
time = ['11:14:54']
voltage = [132.01]
current = [-0.59]
temperature = [22.84]

new_data_row = {'date' : date[0], 'time': time[0], 'voltage' : voltage[0], 'current': current[0], 'temperature' : temperature[0]}

# append mode
with open('log4.csv', 'a') as new_file:
    csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
    csv_writer.writerow(new_data_row)
