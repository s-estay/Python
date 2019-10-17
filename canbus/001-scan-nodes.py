# import canopen
# import time
#
# network = canopen.Network()
# network.connect(channel='can0', bustype='socketcan', bitrate=250000)
#
# network.scanner.search()
# time.sleep(0.05)
# for node_id in network.scanner.nodes:
#     print("Found node %d" % node_id)
#
# network.disconnect()



myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily.get("child1").get("name"))

nodes = dict({"one": {'voltage': 1, 'current': 2}, "two": {'voltage': 3, 'current': 4}})
print(nodes)
print(nodes.get("one"))
print(nodes.get("one").get("voltage"))

nodes = [1, 9, 17]
print(nodes)

for n in nodes:
    print(hex(n + 512))

print(hex(9 + 512))
print(hex(9 + 1792))