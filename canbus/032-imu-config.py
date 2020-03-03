import canopen

network = canopen.Network()
network.connect(channel='/dev/ttyACM2', bustype='slcan', bitrate=250000)

network.send_message(0x204, [0x06, 0x04, 0x01, 0x01])

network.disconnect()
