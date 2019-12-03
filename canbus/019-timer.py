import canopen
import time
import threading
from datetime import datetime


def setup():
    global network
    global nodes
    global nodes_in_network

    network = canopen.Network()
    network.connect(channel='/dev/ttyACM1', bustype='slcan', bitrate=250000)

    nodes_in_network = []
    nodes = {}

    network.scanner.search()
    time.sleep(0.05)
    for node_id in network.scanner.nodes:
        nodes_in_network.append(node_id)
        nodes["node{0}".format(node_id)] = (canopen.RemoteNode(node_id, 'imu-dictionary.eds'))
        network.add_node(nodes["node{0}".format(node_id)])

        network.send_message(node_id + 0x700, [0x00])
        network.send_message(0x00, [0x01, node_id])
        network.send_message(node_id + 0x200, [0x00, 0x03, 0x01, 0xA0, 0x00])


def main_loop():
    all_data = {}
    dateTimeObj = datetime.now()

    print(dateTimeObj, "--------------------------------------------------")
    for x in nodes:
        signed_pack_temperature = nodes[x].sdo[0x4100][4].raw
        pack_temperature = round((100 / 255) * (signed_pack_temperature + 128) - 25, 2)
        pack_current = nodes[x].sdo[0x4100][2].raw
        pack_voltage = nodes[x].sdo[0x4100][1].raw
        pack_data = {x: {"pack_voltage": round(pack_voltage / 100, 5), "pack_current": pack_current, "temperature": pack_temperature}}
        all_data.update(pack_data)
        print(pack_data)

    print('\n')



def printit():
   threading.Timer(5.0, printit).start()
   main_loop()


setup()
printit()