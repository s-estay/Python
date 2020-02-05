import canopen
from datetime import datetime

network = canopen.Network()
network.connect(channel='/dev/ttyACM0', bustype='slcan', bitrate=250000)
node1 = canopen.RemoteNode(1, 'lmu-dictionary.eds')
node2 = canopen.RemoteNode(9, 'lmu-dictionary.eds')
node3 = canopen.RemoteNode(17, 'lmu-dictionary.eds')
network.add_node(node1)
network.add_node(node2)
network.add_node(node3)

network.send_message(0x701, [0x00])
network.send_message(0x709, [0x00])
network.send_message(0x711, [0x00])

network.send_message(0x00, [0x01, 0x01])
network.send_message(0x00, [0x01, 0x09])
network.send_message(0x00, [0x01, 0x11])

network.send_message(0x201, [0x00, 0x03, 0x01, 0xA0, 0x00])
network.send_message(0x209, [0x00, 0x03, 0x01, 0xA0, 0x00])
network.send_message(0x211, [0x00, 0x03, 0x01, 0xA0, 0x00])

dateTimeObj = datetime.now()
print(dateTimeObj, "--------------------------------------------------")

pack_voltage1 = node1.sdo[0x4100][1].raw
print(pack_voltage1/100, "V")

pack_voltage2 = node2.sdo[0x4100][1].raw
print(pack_voltage2/100, "V")

pack_voltage3 = node3.sdo[0x4100][1].raw
print(pack_voltage3/100, "V")

pack_current = node1.sdo[0x4100][2].raw
print(pack_current/100, "A")

pack_pressure = node1.sdo[0x4100][3].raw
print(pack_pressure)

pack_pressure = node2.sdo[0x4100][3].raw
print(pack_pressure)

pack_pressure = node3.sdo[0x4100][3].raw
print(pack_pressure)

signed_pack_temperature = node1.sdo[0x4100][4].raw
pack_temperature = (100/255)*(signed_pack_temperature + 128) - 25
print(round(pack_temperature, 2), "C")

signed_pack_temperature2 = node2.sdo[0x4100][4].raw
pack_temperature2 = (100/255)*(signed_pack_temperature2 + 128) - 25
print(round(pack_temperature2, 2), "C")

signed_pack_temperature3 = node3.sdo[0x4100][4].raw
pack_temperature3 = (100/255)*(signed_pack_temperature3 + 128) - 25
print(round(pack_temperature3, 2), "C")

print('\n')

network.sync.start(1)
network.sync.stop()
network.disconnect()