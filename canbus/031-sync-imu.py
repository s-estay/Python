import canopen

# create network
network = canopen.Network()
network.connect(channel='/dev/ttyACM0', bustype='slcan', bitrate=250000)

# network.send_message(0x80, [0x00])
network.send_message(0x401, [0x01])

from can.listener import Listener

# --

https://github.com/christiansandberg/canopen/blob/61bc0a0874002963233d5401edf9c25fcdcea445/canopen/network.py

Class Network: Representation of one CAN bus containing one or more nodes.

class Network
    def connect(channel, str bustype, int bitrate)
    def add_node(node)
    def send_message(int can_id, data)
    def disconnect()

How we have used the it:

network = canopen.Network()
network.connect(channel='/dev/ttyACM0', bustype='slcan', bitrate=250000)
network.add_node(node1)
network.send_message(0x701, [0x00])
network.disconnect()

# --

Parameter: canopen.Network network
The network to notify on new messages

Class MessageListener: Listens for messages on CAN bus and feeds them to a Network instance.

class MessageListener()
    def on_message_received(msg)

listener = canopen.MessageListener()
listener.on_message_received(msg)

# --

BufferedReader is a subclass of class `~can.Listener`

The messages can then be fetched with can.BufferedReader.get_message

class BufferedReader(Listener)
     def on_message_received(msg) # Append a message to the buffer
     def get_message(timeout=0.5) # Retrieve latest message received

# --

import can
a_listener = can.BufferedReader()
a_listener(generate_message(0xDADADA))
m = a_listener.get_message(0.2)

# --

import can
can_reader = can.BufferedReader()
msg = can_reader.get_message(timeout=0.5)

# --

Class NodeScanner listens for the following messages:
 - Heartbeat (0x700)
 - SDO response (0x580)
 - TxPDO (0x180, 0x280, 0x380, 0x480)
 - EMCY (0x80)

Parameter: canopen.Network network
The network to use when doing active searching.

class canopen.network.NodeScanner()
    def on_message_received(can_id)

# --

scanner = canopen.network.NodeScanner()
scanner.on_message_received(0x586)

# --

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
