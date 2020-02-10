import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.dates import DateFormatter

plt.style.use('seaborn')

data = pd.read_csv('log1.csv', sep='\t')

data['time'] = pd.to_datetime(data['time'])

voltage = data['voltage']
temperature = data['temperature']
time = data['time']

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)

ax1.plot_date(time, voltage, label='Voltage', linewidth=1, linestyle='solid', marker='')
ax2.plot_date(time, temperature, label='Temperature', color='green', linewidth=1, linestyle='solid', marker='')

ax1.set_ylim([110,140])
ax2.set_ylim([20,60])

ax1.legend(loc='upper left')
ax2.legend(loc='upper left')

ax1.set_title('Battery measurement {}'.format(data['time'][0]))

formatter = DateFormatter('%H:%M')
ax1.xaxis.set_major_formatter(formatter)

plt.xticks(rotation=90)

plt.tight_layout()

plt.show()
