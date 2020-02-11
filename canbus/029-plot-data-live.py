import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.dates import DateFormatter
from matplotlib.animation import FuncAnimation

plt.style.use('seaborn')

fig, (ax1, ax2, ax3, ax4) = plt.subplots(nrows=4, ncols=1, sharex=True)

def animate(i):
    data = pd.read_csv('log3.csv', sep='\t')

    data['time'] = pd.to_datetime(data['time'])

    voltage = data['voltage']
    temperature = data['temperature']
    time = data['time']
    current = data['current']
    pressure = data['pressure']

    ax1.clear()
    ax2.clear()
    ax3.clear()
    ax4.clear()

    ax1.plot_date(time, voltage, label='Voltage', linewidth=1, linestyle='solid', marker='')
    ax2.plot_date(time, temperature, label='Temperature', color='green', linewidth=1, linestyle='solid', marker='')
    ax3.plot_date(time, current, label='Current', linewidth=1, linestyle='solid', marker='')
    ax4.plot_date(time, pressure, label='Pressure', linewidth=1, linestyle='solid', marker='')

    ax1.set_ylim([110,150])
    ax2.set_ylim([20,50])
    ax3.set_ylim([-3,3])
    ax4.set_ylim([-5, 15])

    ax1.legend(loc='upper left')
    ax2.legend(loc='upper left')
    ax3.legend(loc='upper left')
    ax4.legend(loc='upper left')

    ax1.set_title('Battery measurement {}'.format(data['time'][0]))

    formatter = DateFormatter('%H:%M')
    ax1.xaxis.set_major_formatter(formatter)

# plt.xticks(rotation=90)

ani = FuncAnimation(fig, animate, interval=1000)

plt.show()
