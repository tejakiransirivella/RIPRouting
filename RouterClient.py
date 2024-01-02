import pickle
import socket
import time


def send_routing_table(client_socket, topology, routers):
    host_address = socket.gethostbyname(socket.gethostname())
    curr_routing_table = routers.get_routing_table(host_address)
    print(curr_routing_table)
    neighbours = topology[host_address]
    for neighbour in neighbours:
        client_socket.sendto(pickle.dumps(curr_routing_table), (neighbour[0], 8080))


def initiate_router(routers, topology):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        while True:
            send_routing_table(client_socket, topology, routers)
            time.sleep(1)  # sleep for 1 second before sending their next update.

    except socket.error as err:
        print(err)
