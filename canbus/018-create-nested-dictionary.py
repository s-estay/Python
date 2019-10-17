import canopen
import time

network = canopen.Network()
network.connect(channel='/dev/ttyACM0', bustype='slcan', bitrate=250000)

nodes_in_network = []
nodes = {}
pack_data = {}
all_data = {}

network.scanner.search()
time.sleep(0.05)
for node_id in network.scanner.nodes:
    nodes_in_network.append(node_id)
    nodes["node{0}".format(node_id)] = (canopen.RemoteNode(node_id, 'lmu-dictionary.eds'))
    network.add_node(nodes["node{0}".format(node_id)])

    network.send_message(node_id + 0x700, [0x00])
    network.send_message(0x00, [0x01, node_id])
    network.send_message(node_id + 0x200, [0x00, 0x03, 0x01, 0xA0, 0x00])

for x in nodes:
    signed_pack_temperature = nodes[x].sdo[0x4100][4].raw
    pack_temperature = round((100 / 255) * (signed_pack_temperature + 128) - 25, 2)
    pack_current = nodes[x].sdo[0x4100][2].raw
    pack_voltage = nodes[x].sdo[0x4100][1].raw
    pack_data = {x: {"pack_voltage": pack_voltage/100, "pack_current": pack_current, "temperature": pack_temperature}}
    all_data.update(pack_data)
    # print(x, pack_voltage / 100, 'V')

print(all_data)
print('found nodes', nodes_in_network)
print(all_data.get("node17").get("pack_voltage"))

network.disconnect()

# print(hex(node_id + 1792))
# print(hex(node_id))
# print(hex(9 + 512))

# nodes = {}
# i = 0
#
# for n in nodes_in_network:
#     nodes[i] = canopen.RemoteNode(n, 'lmu-dictionary.eds')
#     network.add_node(nodes[i])
#     i += 1
#
# print(nodes)

#print(nodes[0])

#all_nodes = dict({"one": {'voltage': nodes.get(0).sdo[0x4100][1].raw/100, 'current': nodes.get(0).sdo[0x4100][2].raw/100}, "two": {'voltage': 3, 'current': 4}})
#print(all_nodes)

#all_nodes = {}
#j = 0

#for n in range(len(nodes_in_network)):
#    all_nodes[] = dict(n)

    #all_nodes = dict({j: {'voltage': nodes.get(n).sdo[0x4100][1].raw/100, 'current': nodes.get(n).sdo[0x4100][2].raw/100, 'temperature': ((100/255)*nodes.get(n).sdo[0x4100][4].raw + 128) - 25}})
    #j += 1

#print(all_nodes)

# nodes = {}
# i = 0
#
# for n in nodes_in_network:
#     nodes[i] = canopen.RemoteNode(n, 'lmu-dictionary.eds')
#     network.add_node(nodes[i])
#     i += 1



    # pack_voltage = nodes.get(n).sdo[0x4100][1].raw
    # print(pack_voltage/100, 'V')
    #
    # pack_current = nodes.get(n).sdo[0x4100][2].raw
    # print(pack_current/100, ' A')
    #
    # signed_pack_temperature = nodes.get(n).sdo[0x4100][4].raw
    # pack_temperature = (100/255)*(signed_pack_temperature + 128) - 25
    # print(round(pack_temperature, 2), '°C')

# nodes = dict({"one": {'voltage': 1, 'current': 2}, "two": {'voltage': 3, 'current': 4}})
# print(nodes)
# print(nodes.get("one"))
# print(nodes.get("one").get("voltage"))

#network.disconnect()









