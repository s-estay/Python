import os

os.system('sudo config-pin p9.24 can')
os.system('sudo config-pin p9.26 can')

os.system('config-pin -q p9.24')
os.system('config-pin -q p9.26')

os.system('sudo ip link set can1 up type can bitrate 250000')
os.system('sudo ifconfig can1 up')

import canopen
import time
import collections

nodes_in_network = []
nodes = {}
all_data = {}
flags = {}


def setup():
    global network
    network = canopen.Network()
    network.connect(bustype='socketcan', channel='can1', bitrate = 250000)
    network.scanner.search()
    time.sleep(0.5)

    for node_id in network.scanner.nodes:
        nodes_in_network.append(node_id)
        nodes["node{0}".format(node_id)] = (canopen.RemoteNode(node_id, 'imu-dictionary.eds'))
        network.add_node(nodes["node{0}".format(node_id)])
        network.send_message(0x200 + node_id, [0x02, 0x00, 0x01, 0x00])

    time.sleep(0.5)
    init_flags()


def init_flags():
    flags_list = [
        "module low",
        "module high",
        "current low",
        "current high",
        "temperature low",
        "temperature high",
        "pressure low",
        "pressure high",
        "module fault",
        "sensor fault",
        "pack low",
        "pack high",
        "internal error",
        "power save mode",
        "startup",
        "heartbeat"]

    flags = dict.fromkeys(flags_list, False)


def flags_node(node_id):
    if node_id in nodes_in_network:
        pack_status_16bits = nodes["node" + str(node_id)].sdo[0x4000].raw
        return '{0:016b}'.format(pack_status_16bits)


def check_flags(node_id):
    if flags_node(node_id)[0] == "1":
        flags["heartbeat"] = True
    if flags_node(node_id)[1] == "1":
        flags["startup"] = True
    if flags_node(node_id)[2] == "1":
        flags["power save mode"] = True
    if flags_node(node_id)[3] == "1":
        flags["internal error"] = True
    if flags_node(node_id)[4] == "1":
        flags["pack high"] = True
    if flags_node(node_id)[5] == "1":
        flags["pack low"] = True
    if flags_node(node_id)[6] == "1":
        flags["sensor fault"] = True
    if flags_node(node_id)[7] == "1":
        flags["module fault"] = True
    if flags_node(node_id)[8] == "1":
        flags["pressure high"] = True
    if flags_node(node_id)[9] == "1":
        flags["pressure low"] = True
    if flags_node(node_id)[10] == "1":
        flags["temperature high"] = True
    if flags_node(node_id)[11] == "1":
        flags["temperature low"] = True
    if flags_node(node_id)[12] == "1":
        flags["current high"] = True
    if flags_node(node_id)[13] == "1":
        flags["current low"] = True
    if flags_node(node_id)[14] == "1":
        flags["module high"] = True
    if flags_node(node_id)[15] == "1":
        flags["module low"] = True

    for key, value in flags.items():
        if value == True:
            print(key)

    print(flags_node(node_id))


setup()
check_flags(1)

network.disconnect()

os.system('sudo ifconfig can1 down')
