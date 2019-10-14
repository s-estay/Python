import canopen

# create network
network = canopen.Network()
network.connect(channel='can0', bustype='socketcan', bitrate=250000)

# send sync request, transmit every 10 ms
network.sync.start(0.01)

network.sync.stop()
network.disconnect()
