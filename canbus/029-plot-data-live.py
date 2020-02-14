import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.dates import DateFormatter
from matplotlib.animation import FuncAnimation

plt.style.use('seaborn')

fig, (ax1, ax2, ax3, ax4) = plt.subplots(nrows=4, ncols=1, sharex=True)

def animate(i):
    data = pd.read_csv('log7.csv', sep='\t')

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

    ax1.plot_date(time, voltage, label='Voltage', color='seagreen', linewidth=1, linestyle='solid', marker='')
    ax2.plot_date(time, temperature, label='Temperature', color='seagreen', linewidth=1, linestyle='solid', marker='')
    ax3.plot_date(time, current, label='Current', color='seagreen', linewidth=1, linestyle='solid', marker='')
    ax4.plot_date(time, pressure, label='Pressure', color='seagreen',linewidth=1, linestyle='solid', marker='')

    ax1.set_ylim([115,145])
    ax2.set_ylim([20,40])
    ax3.set_ylim([-10,10])
    ax4.set_ylim([-5, 15])

    ax1.legend(loc='upper left')
    ax2.legend(loc='upper left')
    ax3.legend(loc='upper left')
    ax4.legend(loc='upper left')

    n = len(data) - 1

    props = dict(boxstyle='round',fc='w', ec='k',lw=0.5, pad=0.25)

    ax1.annotate('{} V'.format(data['voltage'][n]), xy=(data['time'][n], data['voltage'][n]), xytext=(data['time'][n], data['voltage'][n]), bbox=props)
    ax2.annotate('{} °C'.format(data['temperature'][n]), xy=(data['time'][n], data['temperature'][n]), xytext=(data['time'][n], data['temperature'][n]), bbox=props)
    ax3.annotate('{} A'.format(data['current'][n]), xy=(data['time'][n], data['current'][n]), xytext=(data['time'][n], data['current'][n]), bbox=props)
    ax4.annotate('{} bar'.format(data['pressure'][n]), xy=(data['time'][n], data['pressure'][n]), xytext=(data['time'][n], data['pressure'][n]), bbox=props)
    # ax4.annotate('{} bar'.format(data['pressure'][n]), xy=(data['time'][n], data['pressure'][n]), xytext=(data['time'][n] + pd.DateOffset(minutes=11), data['pressure'][n]), bbox=props)

    ax1.set_title('Battery measurement {}'.format(data['time'][0]))

    formatter = DateFormatter('%H:%M')
    ax1.xaxis.set_major_formatter(formatter)

ani = FuncAnimation(fig, animate, interval=1000)

plt.show()
