import canopen

# create network
network = canopen.Network()
network.connect(channel='/dev/ttyACM0', bustype='slcan', bitrate=250000)

# network.send_message(0x80, [0x00])
network.send_message(0x401, [0x01])

from can.listener import Listener

# listener = SomeListener()
# msg = my_bus.recv()
# listener(msg)

# print(canopen.network.MessageListener(network))

# msg = NetworkMessage()
# msg = await reader.get_message()
# print(msg)

# for msg in bus:
#     print(msg.data)


# s = network.get_response()


# class MyListener(can.Listener):
#     def on_message_received(self, msg):
#         print(repr(msg))
#
# network.listeners.append(MyListener())

# on_message_received
