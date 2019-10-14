import canopen
import time

network = canopen.Network()
network.connect(channel='can0', bustype='socketcan', bitrate=250000)

network.scanner.search()
time.sleep(0.05)
for node_id in network.scanner.nodes:
    print("Found node %d" % node_id)

network.disconnect()