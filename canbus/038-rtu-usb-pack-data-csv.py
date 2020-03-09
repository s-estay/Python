import canopen
import time
import csv

nodes_in_network = []
nodes_fieldnames = []
nodes = {}
pack_data = {}
all_pack_data = {}
new_data_row = {}


def setup():
    global network
    network = canopen.Network()
    network.connect(channel='/dev/ttyACM0', bustype='slcan', bitrate=250000)
    network.scanner.search()
    time.sleep(0.5)

    for node_id in network.scanner.nodes:
        nodes_in_network.append(node_id)
        nodes_fieldnames.append("voltage-node{0}".format(node_id))
        nodes_fieldnames.append("current-node{0}".format(node_id))
        nodes_fieldnames.append("temperature-node{0}".format(node_id))
        nodes["node{0}".format(node_id)] = (canopen.RemoteNode(node_id, 'imu-dictionary.eds'))
        network.add_node(nodes["node{0}".format(node_id)])
        network.send_message(0x200 + node_id, [0x02, 0x00, 0x01, 0x00])
        print("Found node %d" % node_id)

    time.sleep(0.5)


def pack_data():
    for n in nodes:
        signed_pack_temperature = nodes[n].sdo[0x4100][3].raw
        pack_temperature = round((1 / 655) * (signed_pack_temperature) - 25, 2)
        pack_current = nodes[n].sdo[0x4100][2].raw
        pack_voltage = nodes[n].sdo[0x4100][1].raw
        pack_data = {n: {"voltage" : pack_voltage/100,
                         "current" : pack_current/100,
                         "temperature" : round(pack_temperature, 2)}}
        all_pack_data.update(pack_data)

    return all_pack_data


def save_to_csv():
    with open('log.csv', 'w') as new_file:
        fieldnames = nodes_fieldnames
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        # loop nodes
        # new_data_row for each one of them
        # append new new_data_row

        for n in nodes:
            new_data_row = {"voltage-{0}".format(n) : pack_data().get(n).get("voltage")}
                            # "current-{0}".format(n) : pack_data().get(n).get("current"),
                            # "temperature-{0}".format(n) : pack_data().get(n).get("temperature")}

            print(new_data_row)
        # csv_writer.writeheader(new_data_row)

    new_file.close()
    print("New measurement saved!")


# print(pack_data().get("node1").get("voltage"))
# print(pack_data().get("node4").get("temperature"))

setup()
# print(pack_data())
# print(nodes_fieldnames)
save_to_csv()

network.disconnect()
