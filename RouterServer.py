import pickle
import socket


def update_routing_table(topology, routers, neighbour_routing_table, curr_router, neighbour_router):
    cost = 0
    for neighbour in topology[curr_router]:
        if neighbour[0] == neighbour_router:
            cost = neighbour[1]
            break

    curr_routing_table = routers.get_routing_table(curr_router)

    for record1 in curr_routing_table.records:
        for record2 in neighbour_routing_table.records:
            if record1.destination == record2.destination and \
                    record1.cost > record2.cost + cost:
                record1.set_next_hop(neighbour_router)
                record1.set_cost(record2.cost + cost)


def initiate_router(routers, topology):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host_address = socket.gethostbyname(socket.gethostname())
    server_socket.bind((host_address, 8080))
    try:
        while True:
            data, neighbour_router = server_socket.recvfrom(2048)
            neighbour_routing_table = pickle.loads(data)
            update_routing_table(topology, routers, neighbour_routing_table, host_address, neighbour_router[0])
    except socket.error as err:
        print(err)
