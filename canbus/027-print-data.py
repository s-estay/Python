import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

plt.style.use('fivethirtyeight')

data = pd.read_csv('log2.csv', sep='\t')

my_time = datetime.strptime(data['time'][0], "%H:%M:%S")
print(my_time.hour)
print(my_time.minute)
print(my_time.second)

data['time'] = pd.to_datetime(data['time'])
print(data['time'][0])
print(data['time'][0].year)
print(data['time'][0].month)
print(data['time'][0].day)
print(data['time'][0].hour)
print(data['time'][0].minute)
print(data['time'][0].second)

print(f"{8:04d}")
print(f"{88:04d}")
print(f"{888:04d}")

voltage = data['voltage']
print(voltage[0])

temperature = data['temperature']
print(temperature[0])
