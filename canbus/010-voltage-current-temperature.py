import canopen

network = canopen.Network()
network.connect(channel='can0', bustype='socketcan', bitrate=250000)
node = canopen.RemoteNode(1, '/path/to/file/lmu-dictionary.eds')
network.add_node(node)

pack_voltage = node.sdo[0x4100][1].raw
print(pack_voltage/100)

pack_current = node.sdo[0x4100][2].raw
print(pack_current/100)

signed_pack_temperature = node.sdo[0x4100][4].raw
pack_temperature = (100/255)*(signed_pack_temperature + 128) - 25
print(pack_temperature)

network.disconnect()
