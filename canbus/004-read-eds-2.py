import canopen

network = canopen.Network()
network.connect(channel='can0', bustype='socketcan', bitrate=250000)
node = canopen.RemoteNode(1, '/path/to/file/imu-dictionary.eds')
network.add_node(node)

vendor_id = node.sdo[0x1018][1].raw
print(hex(vendor_id))

network.disconnect()
