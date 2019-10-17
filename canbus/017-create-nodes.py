import canopen
import time

network = canopen.Network()
network.connect(channel='/dev/ttyACM0', bustype='slcan', bitrate=250000)

nodes_in_network = []

network.scanner.search()
time.sleep(0.05)
for node_id in network.scanner.nodes:
    nodes_in_network.append(node_id)

network.send_message(0x701, [0x00])
network.send_message(0x709, [0x00])
network.send_message(0x711, [0x00])

network.send_message(0x00, [0x01, 0x01])
network.send_message(0x00, [0x01, 0x09])
network.send_message(0x00, [0x01, 0x11])

network.send_message(0x201, [0x00, 0x03, 0x01, 0xA0, 0x00])
network.send_message(0x209, [0x00, 0x03, 0x01, 0xA0, 0x00])
network.send_message(0x211, [0x00, 0x03, 0x01, 0xA0, 0x00])

nodes = {}
i = 0

for n in nodes_in_network:
    nodes[i] = canopen.RemoteNode(n, 'lmu-dictionary.eds')
    network.add_node(nodes[i])
    i += 1

network.disconnect()









