
## Update CANable firmware

There're differents firmwares for the CANable USB-CAN adapter. The wrong one installed might create problems when trying to connect to the RTU. To be on the safe side, update the firmware to the latest release. Go to the [CANable Updater](https://canable.io/updater/) site (works only in Chrome), select `slcan` and follow the instructions.

## Electrical connections

- Connect RTU to router via Ethernet
- Connect CANable (USB-CAN adapter) to RTU via USB
- Connect CANable to the batteries, there's a homemade 3-pins cable to Ethernet pass-through adapter for this purpose
- Give power to RTU (24V) through backplane, which gets its power from a 24V phone regulator OR the batteries
- Connect batteries in series via Ethernet and terminate the bus with a 120 Ohms termination

This will leave the batteries in stand-by. To get data when charging and discharging:

- Connect batteries and the mains switch in series
- Connect charger (use power supply as PV) or inverter (use inductions plates as loads) to EMS
- Switch the mains switch

## Connect to router

- Connect to **Solarbora_5G** WiFi network
- Password: `Hejhopp123`

- Access router's configuration site:
- Default router address: `192.168.2.1`
- User name: `admin`
- Password: `Solarbora`

- In the **clients list**, RTU is:
- Client name: `modio`
- Client IP-adress: `192.168.2.194`

## Connect to RTU

- In the computer's terminal: `ssh root@192.168.2.194 -p 3022`
- Go to Solar Bora's Linux service: `cd /modio/sb-service`
- What's inside? `ls -lh`

## Python requirements

Python libraries:

- CANopen (the main one we're using)
- Can (CANopen builds upon this library)
- aenum (support for advanced enumerations)
- serial (serial communication)

References:
- [CANopen for Python](https://canopen.readthedocs.io/en/latest/) 3/6/2020, 5:42:46 PM
- [python-can](https://python-can.readthedocs.io/en/master/#) 3/6/2020, 5:42:05 PM
- [aenum 2.2.3](https://pypi.org/project/aenum/) 3/6/2020, 5:41:06 PM
- [pySerial](https://pyserial.readthedocs.io/en/latest/) 3/6/2020, 5:47:20 PM

### Install CANopen

CANopen library is a repository that unfortunately can't be directly cloned to the RTU because it doesn't have `git` (and we can't install it). Instead, we can download the repository to our computer and then copy the folder to the RTU via ssh using `scp` (Secure copy protocol):

- In RTU's terminal: `mkdir sb-service`
- Download [CANopen](https://github.com/christiansandberg/canopen) repository
- In computer's terminal: `scp -r -P 3022 canopen root@192.168.2.194:/modio/sb-service`
- In RTU's terminal: `ls -lh /modio/sb-service`
- To copy a folder we add the `-r` option, which tells `scp` to recursively copy the source directory and its contents

References:

- [Use SCP to securely transfer files between two Unix computers](https://kb.iu.edu/d/agye) 3/6/2020, 3:49:57 PM
- [Secure copy protocol](https://en.wikipedia.org/wiki/Secure_copy) 3/6/2020, 3:54:22 PM

## Copy IMU's dictionary

In order to read the pack data and flags from the batteries, we need to store the IMU's electronic data sheet (eds-file):

- In computer's terminal: `scp -P 3022 imu-dictionary.eds root@192.168.2.194:/modio/sb-service`
- In RTU's terminal: `ls -lh /modio/sb-service`

## Recommended workflow

Code locally in your computer and then copy the file to the RTU. Editing Python files directly in the RTU is done in the text editor Nano, which is a little bit annoying.

- Copy Python script to the RTU: `scp -P 3022 code.py root@192.168.2.194:/modio/sb-service` (in computer's terminal)
- Run Python script: `python3 code.py` (in RTU's terminal)

## CSV file

It has a tab `\t` as delimiter. Change it if you don't like it. The default value is a comma (CSV stands for Comma-separated values). The result is saved to `log.csv`. Every time a new measurement is made, `log.csv` will be reseted with new data. Modio want it to work this way.

[Comma-separated values](https://en.wikipedia.org/wiki/Comma-separated_values) 3/10/2020, 12:17:48 PM

## Modio integration

And talking about Modio, their service will run `sb-service.py` in a given interval of time, saving (appending) the output to another csv-file located in a remote server. Modio will keep track of the time, meaning the exact time when each measurement was made.

## Python

Everything is coded with dynamic-variable-creation in mind.

### Scan nodes

Run it: `python3 034-rtu-usb-scan-nodes.py`

```
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
```

Which will print:

```
Found node 1
Found node 2
Found node 4
```

To determine the USB port used by the USB-CAN adapter: `ls /dev/ttyACM*`

### Flags

Run it: `python3 035-rtu-usb-flags.py`

```
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
    network.connect(channel='/dev/ttyACM0', bustype='slcan', bitrate=250000)
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
```

Which will print:

```
startup
heartbeat
1100000000000000
```

### Pack data

Run it: `python3 036-rtu-usb-pack-data.py`

```
import canopen
import time

nodes_in_network = []
nodes = {}
pack_data = {}
all_data = {}


def setup():
    global network
    network = canopen.Network()
    network.connect(channel='/dev/ttyACM0', bustype='slcan', bitrate=250000)
    network.scanner.search()
    time.sleep(0.5)

    for node_id in network.scanner.nodes:
        nodes_in_network.append(node_id)
        nodes["node{0}".format(node_id)] = (canopen.RemoteNode(node_id, 'imu-dictionary.eds'))
        network.add_node(nodes["node{0}".format(node_id)])
        network.send_message(0x200 + node_id, [0x02, 0x00, 0x01, 0x00])

    time.sleep(0.5)


def pack_data():
    for x in nodes:
        signed_pack_temperature = nodes[x].sdo[0x4100][3].raw
        pack_temperature = round((1 / 655) * (signed_pack_temperature) - 25, 2)
        pack_current = nodes[x].sdo[0x4100][2].raw
        pack_voltage = nodes[x].sdo[0x4100][1].raw
        pack_data = {x: {"voltage": pack_voltage/100, "current": pack_current/100, "temperature": pack_temperature}}
        all_data.update(pack_data)
    return all_data


setup()
print(pack_data())
print(pack_data().get("node1").get("voltage"))
print(pack_data().get("node4").get("temperature"))

network.disconnect()
```

Which will print:

```
{'node1': {'voltage': 152.06, 'current': 0.0, 'temperature': 22.2}, 'node4': {'voltage': 152.0, 'current': 0.09, 'temperature': 21.84}, 'node2': {'voltage': 152.0, 'current': 0.0, 'temperature': 21.97}}
152.06
21.84
```
