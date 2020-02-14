import csv
import time
import canopen
import threading
from datetime import datetime


def setup():
    global network
    global node

    network = canopen.Network()
    network.connect(channel='/dev/ttyACM0', bustype='slcan', bitrate=250000)

    network.send_message(0x201, [0x00, 0x03, 0x01, 0xA0, 0x00])

    node = canopen.RemoteNode(1, 'imu-dictionary.eds')
    network.add_node(node)

    # network.send_message(0x701, [0x00])
    # network.send_message(0x00, [0x01, 0x01])


def main_loop():
    date = datetime.now().strftime("%Y-%m-%d")
    time = datetime.now().strftime("%H:%M:%S")

    pack_voltage = node.sdo[0x4100][1].raw
    pack_current = node.sdo[0x4100][2].raw
    signed_pack_temperature = node.sdo[0x4100][3].raw
    pack_temperature = round((1 / 655) * (signed_pack_temperature) - 25, 2)
    pressure = 0

    # pack_pressure = node.sdo[0x4100][3].raw
    # pressure = pack_pressure*(12/65500) - 2

    new_data_row = {'time' : time, 'voltage' : pack_voltage/100, 'temperature' : pack_temperature, 'current' : pack_current/100, 'pressure' : pressure}

    # csv append mode
    with open('log6.csv', 'a') as new_file:
        fieldnames = ['time', 'voltage', 'temperature', 'current', 'pressure']
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
        csv_writer.writerow(new_data_row)

    new_file.close()


def printit():
   threading.Timer(5.0, printit).start()
   main_loop()


setup()
printit()
