
## Electrical connections

- Connect BBG to router via Ethernet
- Connect CAN transceiver to BBG
- Give power to CAN transceiver (5V, 3V3 and GND) from an Arduino connected to the router
- Connect CAN transceiver to Ethernet-CAN pass-through adapter
- Connect Ethernet-CAN pass-through adapter to one battery
- Connect batteries in series via Ethernet and terminate the bus with a 120 Ohms termination
- Connect batteries and the mains switch in series
- Give power to batteries (24V and GND) from the EMS
- Switch the mains switch

## BBG configuration

- Connect computer to Solarbora_5G WiFi network
  - Password: Hejhopp123

- Access BBG: `$ sudo ssh debian@beaglebone.local`
  - Enter computer's password
  - Enter BBG's password BBG: temppwd

Login as super user: `$ sudo su`

Set UART1 pins as CAN bus:
```
$ config-pin p9.24 can
$ config-pin p9.26 can
```

Test if correct:
```
$ config-pin -q p9.24
P9_24 Mode: can
$ config-pin -q p9.26
P9_26 Mode: can
```

## Python

### Scan nodes

Lets see what we got in the BBG:
```
$ ls
01-scan-nodes.py
02-config-can-scan.py
03-pack-data.py
04-flags.py
imu-dictionary.eds
```

Run `01-scan-nodes.py` to scan nodes in the network:
```
$ python3 01-scan-nodes.py
Found node 1
Found node 2
Found node 4
```

If you don't have CANopen installed, do: `pip3 install canopen`

What's inside `01-scan-nodes.py`?:
```
import os

os.system('sudo ip link set can1 up type can bitrate 250000')
os.system('sudo ifconfig can1 up')

import canopen
import time

network = canopen.Network()
network.connect(bustype='socketcan', channel='can1', bitrate = 250000)

network.scanner.search()

time.sleep(0.05)
for node_id in network.scanner.nodes:
        print("Found node %d" % node_id)

network.disconnect()

os.system('sudo ifconfig can1 down')
```

### Configure and scan

Configure CAN bus pins and scan nodes:
```
$ python3 02-config-can-scan.py
P9_24 Mode: can
P9_26 Mode: can
Found node 1
Found node 2
Found node 4
```

What's inside `02-config-can-scan.py`?:
```
import os

os.system('sudo config-pin p9.24 can')
os.system('sudo config-pin p9.26 can')

os.system('config-pin -q p9.24')
os.system('config-pin -q p9.26')

os.system('sudo ip link set can1 up type can bitrate 250000')
os.system('sudo ifconfig can1 up')

import canopen
import time

network = canopen.Network()
network.connect(bustype='socketcan', channel='can1', bitrate = 250000)

network.scanner.search()

time.sleep(0.05)
for node_id in network.scanner.nodes:
        print("Found node %d" % node_id)

network.disconnect()

os.system('sudo ifconfig can1 down')
```

### Pack data

Get pack data:
```
$ python3 03-pack-data.py
P9_24 Mode: can
P9_26 Mode: can
Nodes in network:  [1, 2, 4]
{'node1': {'temperature': 21.27, 'pack_current': -0.04, 'pack_voltage': 152.84}, 'node4': {'temperature': 20.98, 'pack_current': 0.03, 'pack_voltage': 152.66}, 'node2': {'temperature': 21.08, 'pack_current': 0.0, 'pack_voltage': 152.72}}
```

Shit don't work? You have to have eds-dictionary **imu-dictionary.eds**.

What's inside `03-pack-data.py`?:
```
import os

os.system('sudo config-pin p9.24 can')
os.system('sudo config-pin p9.26 can')

os.system('config-pin -q p9.24')
os.system('config-pin -q p9.26')

os.system('sudo ip link set can1 up type can bitrate 250000')
os.system('sudo ifconfig can1 up')

import canopen
import time

network = canopen.Network()
network.connect(bustype='socketcan', channel='can1', bitrate = 250000)

nodes_in_network = []
nodes = {}
pack_data = {}
all_data = {}

network.scanner.search()
time.sleep(0.5)

for node_id in network.scanner.nodes:
    nodes_in_network.append(node_id)
    nodes["node{0}".format(node_id)] = (canopen.RemoteNode(node_id, 'imu-dictionary.eds'))
    network.add_node(nodes["node{0}".format(node_id)])

    network.send_message(0x200 + node_id, [0x02, 0x00, 0x01, 0x00])

time.sleep(0.5)

for x in nodes:
    signed_pack_temperature = nodes[x].sdo[0x4100][3].raw
    pack_temperature = round((1 / 655) * (signed_pack_temperature) - 25, 2)
    pack_current = nodes[x].sdo[0x4100][2].raw
    pack_voltage = nodes[x].sdo[0x4100][1].raw
    pack_data = {x: {"pack_voltage": pack_voltage/100, "pack_current": pack_current/100, "temperature": pack_temperature}}
    all_data.update(pack_data)

print('Nodes in network: ', nodes_in_network)
print(all_data)

network.disconnect()

os.system('sudo ifconfig can1 down')
```

This Python file prints a whole dictionary: `print(all_data)`

To get just one value: `print(all_data.get("node4").get("pack_voltage"))`

### Flags

Get flags:
```
$ python3 04-flags.py
P9_24 Mode: can
P9_26 Mode: can
startup
0100000000000000
```

In this case only the **startup** flag was set, which is bit 14 in the status pack register.

What's inside `04-flags.py`?:
```
import os

os.system('sudo config-pin p9.24 can')
os.system('sudo config-pin p9.26 can')

os.system('config-pin -q p9.24')
os.system('config-pin -q p9.26')

os.system('sudo ip link set can1 up type can bitrate 250000')
os.system('sudo ifconfig can1 up')

import canopen
import time
import collections

nodes_in_network = []
nodes = {}
all_data = {}
flags = {}


def setup():
    global network
    network = canopen.Network()
    network.connect(bustype='socketcan', channel='can1', bitrate = 250000)
    network.scanner.search()
    time.sleep(0.5)

    for node_id in network.scanner.nodes:
        nodes_in_network.append(node_id)
        nodes["node{0}".format(node_id)] = (canopen.RemoteNode(node_id, 'imu-dictionary.eds'))
        network.add_node(nodes["node{0}".format(node_id)])
        network.send_message(0x200 + node_id, [0x02, 0x00, 0x01, 0x00])

    time.sleep(0.5)
    init_flags()


def init_flags():
    flags_list = [
        "module low",
        "module high",
        "current low",
        "current high",
        "temperature low",
        "temperature high",
        "pressure low",
        "pressure high",
        "module fault",
        "sensor fault",
        "pack low",
        "pack high",
        "internal error",
        "power save mode",
        "startup",
        "heartbeat"]

    flags = dict.fromkeys(flags_list, False)


def flags_node(node_id):
    if node_id in nodes_in_network:
        pack_status_16bits = nodes["node" + str(node_id)].sdo[0x4000].raw
        return '{0:016b}'.format(pack_status_16bits)


def check_flags(node_id):
    if flags_node(node_id)[0] == "1":
        flags["heartbeat"] = True
    if flags_node(node_id)[1] == "1":
        flags["startup"] = True
    if flags_node(node_id)[2] == "1":
        flags["power save mode"] = True
    if flags_node(node_id)[3] == "1":
        flags["internal error"] = True
    if flags_node(node_id)[4] == "1":
        flags["pack high"] = True
    if flags_node(node_id)[5] == "1":
        flags["pack low"] = True
    if flags_node(node_id)[6] == "1":
        flags["sensor fault"] = True
    if flags_node(node_id)[7] == "1":
        flags["module fault"] = True
    if flags_node(node_id)[8] == "1":
        flags["pressure high"] = True
    if flags_node(node_id)[9] == "1":
        flags["pressure low"] = True
    if flags_node(node_id)[10] == "1":
        flags["temperature high"] = True
    if flags_node(node_id)[11] == "1":
        flags["temperature low"] = True
    if flags_node(node_id)[12] == "1":
        flags["current high"] = True
    if flags_node(node_id)[13] == "1":
        flags["current low"] = True
    if flags_node(node_id)[14] == "1":
        flags["module high"] = True
    if flags_node(node_id)[15] == "1":
        flags["module low"] = True

    for key, value in flags.items():
        if value == True:
            print(key)

    print(flags_node(node_id))


setup()
check_flags(1)

network.disconnect()
os.system('sudo ifconfig can1 down')
```
