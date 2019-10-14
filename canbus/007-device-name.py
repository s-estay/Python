import canopen

network = canopen.Network()
network.connect(channel='can0', bustype='socketcan', bitrate=250000)
node = canopen.RemoteNode(9, '/path/to/file/canbus-test/imu-dictionary.eds')
network.add_node(node)

device_name = node.sdo['DeviceName'].raw
print(device_name)

network.sync.start(1)
network.sync.stop()
network.disconnect()
