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

    node = canopen.RemoteNode(1, 'lmu-dictionary.eds')
    network.add_node(node)

    network.send_message(0x701, [0x00])
    network.send_message(0x00, [0x01, 0x01])
    network.send_message(0x201, [0x00, 0x03, 0x01, 0xA0, 0x00])


def main_loop():
    date = datetime.now().strftime("%Y-%m-%d")
    time = datetime.now().strftime("%H:%M:%S")

    pack_voltage = node.sdo[0x4100][1].raw
    signed_pack_temperature = node.sdo[0x4100][4].raw
    pack_temperature = (100/255)*(signed_pack_temperature + 128) - 25

    new_data_row = {'time' : 'time', 'voltage' : pack_voltage/100, 'temperature' : round(pack_temperature, 2)}

    # csv append mode
    with open('log1.csv', 'a') as new_file:
        fieldnames = ['time', 'voltage', 'temperature']
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
        csv_writer.writerow(new_data_row)

    new_file.close()


def printit():
   threading.Timer(5.0, printit).start()
   main_loop()


setup()
printit()
