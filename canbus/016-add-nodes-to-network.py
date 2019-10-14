import canopen
import time

network = canopen.Network()
network.connect(channel='/dev/ttyACM0', bustype='slcan', bitrate=250000)

nodes_in_network = []

network.scanner.search()
time.sleep(0.05)
for node_id in network.scanner.nodes:
    nodes_in_network.append(node_id)

for n in nodes_in_network:
    network.add_node(n)

network.disconnect()