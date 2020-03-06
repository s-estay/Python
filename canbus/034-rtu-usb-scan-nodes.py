import canopen
import time

network = canopen.Network()
network.connect(channel='/dev/ttyACM0', bustype='slcan', bitrate=250000)
network.scanner.search()
time.sleep(0.5)

for node_id in network.scanner.nodes:
    network.send_message(0x200 + node_id, [0x02, 0x00, 0x01, 0x00])
    print("Found node %d" % node_id)

network.disconnect()
