
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
- `$ sudo ssh debian@beaglebone.local`
  - Password: temppwd

Set UART1 pins as CAN bus:
```
$ sudo config-pin p9.24 can
$ sudo config-pin p9.26 can
```

Test if correct:
```
$ config-pin -q p9.24
P9_24 Mode: can
$ config-pin -q p9.26
P9_26 Mode: can
```

## Scan nodes

Lets see what we got in the BBG:
```
$ ls
01-scan-nodes.py
```

Run that Python script to scan nodes in the network:
```
$ python3 01-scan-nodes.py
Found node 1
Found node 2
Found node 4
```

What is inside `01-scan-nodes.py`?:
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

## Configure and scan

Configure CAN bus pins and scan nodes:
```
$ python3 02-config-can-scan.py
P9_24 Mode: can
P9_26 Mode: can
Found node 1
Found node 2
Found node 4
```

What is inside `02-config-can-scan.py`?:
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
