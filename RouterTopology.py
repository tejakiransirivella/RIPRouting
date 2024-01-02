# coding=utf-8
from Record import Record
from Routers import Routers
from RoutingTable import RoutingTable


def generate_routing_tables():
    mask = "255.255.255.0"
    addresses = ["129.21.30.37", "129.21.34.80", "129.21.37.49", "129.21.22.196"]
    routers = Routers()

    for address1 in addresses:
        routing_table = RoutingTable()
        for address2 in addresses:
            if address1 != address2:
                routing_table.add_record(Record(address2, "Unavailable", mask, 16))
            else:
                routing_table.add_record(Record(address2, "0.0.0.0", mask, 0))
        routers.add_routing_table(address1, routing_table)
    return routers


def generate_routing_topology(cost):
    addresses = ["129.21.30.37", "129.21.34.80", "129.21.37.49", "129.21.22.196"]
    topology = {}
    for index in range(len(addresses)):
        topology[addresses[index]] = []
        prev = (index - 1 + len(addresses)) % len(addresses)
        topology[addresses[index]].append((addresses[prev], cost[prev]))
        next = (index + 1) % len(addresses)
        topology[addresses[index]].append((addresses[next], cost[index]))
    return topology


def test():
    routers = generate_routing_tables()
    print(routers)


# test()
