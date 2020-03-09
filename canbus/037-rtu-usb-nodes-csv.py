import canopen
import time
import csv

nodes_in_network = []
nodes_fieldnames = []
nodes = {}


def setup():
    global network
    network = canopen.Network()
    network.connect(channel='/dev/ttyACM0', bustype='slcan', bitrate=250000)
    network.scanner.search()
    time.sleep(0.5)

    for node_id in network.scanner.nodes:
        nodes_in_network.append(node_id)
        nodes_fieldnames.append("node{0}".format(node_id))
        nodes["node{0}".format(node_id)] = (canopen.RemoteNode(node_id, 'imu-dictionary.eds'))
        network.add_node(nodes["node{0}".format(node_id)])
        network.send_message(0x200 + node_id, [0x02, 0x00, 0x01, 0x00])
        print("Found node %d" % node_id)

    time.sleep(0.5)


def save_to_csv():
    with open('log.csv', 'w') as new_file:
        fieldnames = nodes_fieldnames
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
        csv_writer.writeheader()

    new_file.close()
    print("New measurement saved!")


setup()
save_to_csv()

network.disconnect()
