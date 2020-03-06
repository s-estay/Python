import canopen
import time

nodes_in_network = []
nodes = {}
pack_data = {}
all_data = {}


def setup():
    global network
    network = canopen.Network()
    network.connect(channel='/dev/ttyACM0', bustype='slcan', bitrate=250000)
    network.scanner.search()
    time.sleep(0.5)

    for node_id in network.scanner.nodes:
        nodes_in_network.append(node_id)
        nodes["node{0}".format(node_id)] = (canopen.RemoteNode(node_id, 'imu-dictionary.eds'))
        network.add_node(nodes["node{0}".format(node_id)])
        network.send_message(0x200 + node_id, [0x02, 0x00, 0x01, 0x00])

    time.sleep(0.5)


def pack_data():
    for x in nodes:
        signed_pack_temperature = nodes[x].sdo[0x4100][3].raw
        pack_temperature = round((1 / 655) * (signed_pack_temperature) - 25, 2)
        pack_current = nodes[x].sdo[0x4100][2].raw
        pack_voltage = nodes[x].sdo[0x4100][1].raw
        pack_data = {x: {"voltage": pack_voltage/100, "current": pack_current/100, "temperature": pack_temperature}}
        all_data.update(pack_data)
    return all_data


setup()
print(pack_data())
print(pack_data().get("node1").get("voltage"))
print(pack_data().get("node4").get("temperature"))

network.disconnect()
