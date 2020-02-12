# sudo chmod 666 /dev/ttyACM0

import canopen
import csv

network = canopen.Network()
network.connect(channel='/dev/ttyACM1', bustype='slcan', bitrate=250000)

# TODO: add scan nodes

node = canopen.RemoteNode(1, 'lmu-dictionary.eds')
network.add_node(node)

network.send_message(0x701, [0x00])
network.send_message(0x00, [0x01, 0x01])
network.send_message(0x201, [0x00, 0x03, 0x01, 0xA0, 0x00])

# csv write mode
with open('log6.csv', 'w') as new_file:
    fieldnames = ['time', 'voltage', 'temperature', 'current', 'pressure']
    csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
    csv_writer.writeheader()

new_file.close()

network.sync.start(1)
network.sync.stop()
network.disconnect()
