import canopen

network = canopen.Network()
network.connect(channel='can0', bustype='socketcan', bitrate=250000)
node = canopen.RemoteNode(1, '/path/to/file/imu-dictionary.eds')
network.add_node(node)

node.sdo['ProducerHeartbeatTime'].raw = 1000

network.disconnect()
