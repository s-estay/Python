import canopen

network = canopen.Network()
network.connect(channel='can0', bustype='socketcan', bitrate=250000)
node = canopen.RemoteNode(9, '/path/to/file/canbus-test/imu-dictionary.eds')
network.add_node(node)

network.send_message(0x201, [0x00, 0x03, 0x01, 0xA0, 0x00])

network.disconnect()
