import canopen
import time
import csv

nodes_fieldnames = []
nodes = {}


def setup():
    global network
    network = canopen.Network()
    network.connect(channel = '/dev/ttyACM0', bustype = 'slcan', bitrate = 250000)
    network.scanner.search()
    time.sleep(0.5)

    nodes_in_network = []

    for node_id in network.scanner.nodes:
        nodes_in_network.append(node_id)
        nodes_fieldnames.append("voltage-node{0}".format(node_id))
        nodes_fieldnames.append("current-node{0}".format(node_id))
        nodes_fieldnames.append("temperature-node{0}".format(node_id))
        nodes_fieldnames.append("flags-node{0}".format(node_id))
        nodes["node{0}".format(node_id)] = (canopen.RemoteNode(node_id, 'imu-dictionary.eds'))
        network.add_node(nodes["node{0}".format(node_id)])
        network.send_message(0x200 + node_id, [0x02, 0x00, 0x01, 0x00])
        print("Found node %d" % node_id)

    time.sleep(0.5)


def node_flags():
    all_node_flags = {}

    for n in nodes:
        pack_status_16bits = nodes[n].sdo[0x4000].raw
        new_row = {n : {"flags" : '{0:016b}'.format(pack_status_16bits)}}
        all_node_flags.update(new_row)

    return all_node_flags


def pack_data():
    all_pack_data = {}

    for n in nodes:
        signed_pack_temperature = nodes[n].sdo[0x4100][3].raw
        pack_temperature = round((1 / 655) * (signed_pack_temperature) - 25, 2)
        pack_current = nodes[n].sdo[0x4100][2].raw
        pack_voltage = nodes[n].sdo[0x4100][1].raw
        new_row = {n : {"voltage" : pack_voltage/100,
                         "current" : pack_current/100,
                         "temperature" : round(pack_temperature, 2)}}
        all_pack_data.update(new_row)

    return all_pack_data


def save_to_csv():
    new_data_row = {}

    with open('log.csv', 'w') as new_file:
        fieldnames = nodes_fieldnames
        csv_writer = csv.DictWriter(new_file, fieldnames = fieldnames, delimiter = '\t')
        csv_writer.writeheader()

        pd = pack_data()
        fn = node_flags()

        for n in nodes:
            new_data_row.update({"voltage-{0}".format(n) : pd.get(n).get("voltage")})
            new_data_row.update({"current-{0}".format(n) : pd.get(n).get("current")})
            new_data_row.update({"temperature-{0}".format(n) : pd.get(n).get("temperature")})
            new_data_row.update({"flags-{0}".format(n) : fn.get(n).get("flags")})

        csv_writer.writerow(new_data_row)

    new_file.close()
    print("New measurement saved!")


setup()
save_to_csv()


network.disconnect()
