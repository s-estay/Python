import canopen

network = canopen.Network()
network.connect(channel='can0', bustype='socketcan', bitrate=250000)
node = canopen.RemoteNode(1, '/path/to/file/lmu-dictionary.eds')
network.add_node(node)

pack_voltage = node.sdo[0x4100][1].raw
print(pack_voltage/100)

network.disconnect()
