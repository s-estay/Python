import canopen

network = canopen.Network()
network.connect(channel='can0', bustype='socketcan', bitrate=250000)
node = canopen.RemoteNode(1, '/path/to/file/lmu-dictionary.eds')
network.add_node(node)

pack_temperature = node.sdo[0x4100][4]
print(pack_temperature.raw)

network.disconnect()
