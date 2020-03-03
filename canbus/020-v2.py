import canopen
import time

network = canopen.Network()
network.connect(channel='/dev/ttyACM2', bustype='slcan', bitrate=250000)

network.send_message(0x201, [0x02, 0x00, 0x01, 0x00])
network.send_message(0x202, [0x02, 0x00, 0x01, 0x00])
network.send_message(0x204, [0x02, 0x00, 0x01, 0x00])

# node1 = canopen.RemoteNode(9, 'lmu-dictionary.eds')
# print(node1)
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

# print('Nodes in network: ', nodes_in_network)

for x in nodes:
    print(x)

    signed_pack_temperature = nodes[x].sdo[0x4100][3].raw
    pack_temperature = round((1 / 655) * (signed_pack_temperature) - 25, 2)
    print('{}C'.format(pack_temperature))
    pack_current = nodes[x].sdo[0x4100][2].raw
    print('{}A'.format(pack_current/100))
    pack_voltage = nodes[x].sdo[0x4100][1].raw
    print('{}V'.format(pack_voltage/100))
    # pack_pressure = nodes[x].sdo[0x4100][3].raw
    # print(pack_pressure)
    # print('{} bar'.format(pack_pressure*(12/65500) - 2))
    pack_data = {x: {"pack_voltage": pack_voltage/100, "pack_current": pack_current/100, "temperature": pack_temperature}}
    all_data.update(pack_data)
    # print(x, pack_voltage / 100, 'V')
    print('\n')


# print(all_data)
# print('Nodes in network: ', nodes_in_network)
# print(all_data.get("node1").get("pack_voltage"))
# print(all_data.get("node1").get("pack_current"))
# print(all_data.get("node1").get("pack_temperature"))

network.disconnect()
