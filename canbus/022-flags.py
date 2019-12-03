import canopen
import time

nodes = {}
nodes_in_network = []
all_data = {}


def setup():
    network = canopen.Network()
    network.connect(channel='/dev/ttyACM0', bustype='slcan', bitrate=250000)
    network.scanner.search()
    time.sleep(0.05)
    for node_id in network.scanner.nodes:
        nodes_in_network.append(node_id)
        network.send_message(0x200 + node_id, [0x02, 0x00, 0x01, 0x00]) # set power save mode
        nodes["node{0}".format(node_id)] = (canopen.RemoteNode(node_id, 'imu-dictionary.eds'))
        network.add_node(nodes["node{0}".format(node_id)])


def read():
    for n in nodes:
        signed_pack_temperature = nodes[n].sdo[0x4100][3].raw
        pack_temperature = round((1 / 655) * signed_pack_temperature - 25, 2)
        pack_current = nodes[n].sdo[0x4100][2].raw
        pack_voltage = nodes[n].sdo[0x4100][1].raw
        pack_data = {n: {"pack_voltage": pack_voltage / 100, "pack_current": pack_current / 100,
                         "pack_temperature": pack_temperature}}
        all_data.update(pack_data)

    print('Nodes in network: ', nodes_in_network)
    #print(all_data)


def flag_node(node_id):
    if "node" + str(node_id) in all_data:
        pack_status_16bits = nodes["node" + str(node_id)].sdo[0x4000].raw
        return '{0:016b}'.format(pack_status_16bits)


def flag_all_nodes():
    flag_list = []
    for node_id in nodes_in_network:
        pack_status_16bits = nodes["node" + str(node_id)].sdo[0x4000].raw
        flag_list.append('{0:016b}'.format(pack_status_16bits))
    return flag_list


def data_node(node_id, value):
    if "node"+str(node_id) in all_data:
        return all_data.get("node"+str(node_id)).get(value)
    else:
        print("no")


def data_all_nodes(value):
    value_list = []
    for n in nodes_in_network:
        value_list.append(all_data.get("node"+str(n)).get(value))
    return value_list


setup()
read()


print(data_node(4, "pack_voltage"))
print(data_all_nodes("pack_temperature"))
print(flag_node(2))
print(flag_all_nodes())


################################################################################

# this_dictionary = {"brand": "Ford", "model": "Mustang", "year": 1964}
# print(this_dictionary)
#
#
# def key_test(key):
#     if key in this_dictionary:
#         print("yes, " + this_dictionary.get(key))
#     else:
#         print("no")
#
#
# key_test("brand")
# key_test("colour")

################################################################################

# for n in nodes:


#     for b in pack_status_16bits:
#         if pack_status_16bits[15]:
#             module_low = True
#         if pack_status_16bits[14]:
#             module_high = True
#         if pack_status_16bits[13]:
#             current_low = True
#         if pack_status_16bits[12]:
#             current_high = True
#         if pack_status_16bits[11]:
#             temperature_low = True
#         if pack_status_16bits[10]:
#             temperature_high = True
#         if pack_status_16bits[9]:
#             pressure_low = True
#         if pack_status_16bits[8]:
#             pressure_high = True
#         if pack_status_16bits[7]:
#             module_fault = True
#         if pack_status_16bits[6]:
#             sensor_fault = True
#         if pack_status_16bits[5]:
#             pack_low = True
#         if pack_status_16bits[4]:
#             pack_high = True
#         if pack_status_16bits[3]:
#             internal_error = True
#         if pack_status_16bits[2]:
#             power_save_mode = True
#         if pack_status_16bits[1]:
#             startup = True
#         if pack_status_16bits[0]:
#             heartbeat = True

################################################################################

# thislist = ["low module voltage", "banana", "cherry"]
# thislist[0] = 1
# thislist[1] = 0
# thislist[2] = 1

# for n in nodes:
#     pack_status = nodes[n].sdo[0x4000].raw
#     pack_status_16bits = '{0:016b}'.format(pack_status)
#
#     for b in pack_status_16bits:
#         if b == 1:
#            print(index[b])

