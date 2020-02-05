import canopen
import time

network = canopen.Network()
network.connect(channel='/dev/ttyACM0', bustype='slcan', bitrate=250000)

network.scanner.search()
time.sleep(0.05)
for node_id in network.scanner.nodes:
    print("Found node %d" % node_id)

pack_voltage = node.sdo[0x4100][1].raw
print(pack_voltage/100)

network.disconnect()