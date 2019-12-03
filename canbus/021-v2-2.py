import canopen
import time

network = canopen.Network()
network.connect(channel='/dev/ttyACM0', bustype='slcan', bitrate=250000)

network.send_message(0x201, [0x02, 0x00, 0x01, 0x00])
network.send_message(0x202, [0x02, 0x00, 0x01, 0x00])
network.send_message(0x204, [0x02, 0x00, 0x01, 0x01])

nodes_in_network = []
nodes = {}
pack_data = {}
all_data = {}

network.scanner.search()
time.sleep(0.05)
for node_id in network.scanner.nodes:
    nodes_in_network.append(node_id)
    nodes["node{0}".format(node_id)] = (canopen.RemoteNode(node_id, 'imu-dictionary.eds'))
    network.add_node(nodes["node{0}".format(node_id)])

print('Nodes in network: ', nodes_in_network)

for x in nodes:
    print(nodes_in_network[0])
    print(x)
    pack_status = nodes[x].sdo[0x4000].raw
    print('{0:016b}'.format(pack_status))

    pack_status_16bits = '{0:016b}'.format(pack_status)
    heart_beat = pack_status_16bits[0]
    print(heart_beat)

network.disconnect()