import canopen

network = canopen.Network()
network.connect(channel='can0', bustype='socketcan', bitrate=250000)
node = canopen.RemoteNode(1, '/path/to/file/imu-dictionary.eds')
network.add_node(node)

id = int(0x1400)
COB_ID = node.sdo[id][1]
TRANSMISSION_TYPE = node.sdo[id][2]

print(hex(COB_ID.raw))
print(TRANSMISSION_TYPE.raw)

network.sync.start(1)
network.sync.stop()
network.disconnect()
