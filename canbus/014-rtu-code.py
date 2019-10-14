import canopen

network = canopen.Network()
network.connect(channel='/dev/ttyACM0', bustype='slcan', bitrate=250000)
node = canopen.RemoteNode(9, '/home/sebastian/Documents/canbus/lmu-dictionary.eds')
network.add_node(node)

network.send_message(0x701, [0x00])
network.send_message(0x709, [0x00])
network.send_message(0x711, [0x00])

network.send_message(0x00, [0x01, 0x01])
network.send_message(0x00, [0x01, 0x09])
network.send_message(0x00, [0x01, 0x11])

network.send_message(0x201, [0x00, 0x03, 0x01, 0xA0, 0x00])
network.send_message(0x209, [0x00, 0x03, 0x01, 0xA0, 0x00])
network.send_message(0x211, [0x00, 0x03, 0x01, 0xA0, 0x00])

pack_voltage = node.sdo[0x4100][1].raw
print(pack_voltage/100, 'V')

pack_current = node.sdo[0x4100][2].raw
print(pack_current/100, ' A')

signed_pack_temperature = node.sdo[0x4100][4].raw
pack_temperature = (100/255)*(signed_pack_temperature + 128) - 25
print(round(pack_temperature, 2), '°C')

network.sync.start(1)
network.sync.stop()
network.disconnect()
