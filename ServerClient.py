# coding=utf-8
import socket
from threading import Thread

import RouterClient
import RouterServer
import RouterTopology


def main():
    input_cost = raw_input("Enter cost between links followed by a space ")
    input_cost_list = input_cost.split(" ")
    cost = []
    for input_cost in input_cost_list:
        cost.append(int(input_cost))

    topology = RouterTopology.generate_routing_topology(cost)
    routers = RouterTopology.generate_routing_tables()

    host_address = socket.gethostbyname(socket.gethostname())
    curr_routing_table = routers.get_routing_table(host_address)

    for record in curr_routing_table.records:
        neighbours = topology[host_address]
        for neighbour in neighbours:
            if neighbour[0] == record.destination:
                record.set_cost(neighbour[1])
                record.set_next_hop(neighbour[0])

    client = Thread(target=RouterClient.initiate_router, args=(routers, topology))
    server = Thread(target=RouterServer.initiate_router, args=(routers, topology))

    server.start()
    client.start()


main()
