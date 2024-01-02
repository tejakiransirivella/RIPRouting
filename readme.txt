RouterCommunication:
--------------------
This project implements distance-vector routing protocol called RIP.

Prerequisites:
--------------
1. Python version 2.7.18

Project Structure:
-----------------

ServerClient - This is a main program that initializes both server(receive route updates) and
client(send route updates)
RouterClient - This handles client side of the program sending route updates to its neighbours.
RouterServer - This handles server side of the program receiving route updates from its neighbours
and updates the routing tables if route is optimal
RouterTopology : This creates a topology and creates routing tables for a router based on topology
Routers,RoutingTable,Record : These are classes that stores the routing tables information and prints them.

Program Execution:
------------------
Execute ServerClient.py on all router machines and give the cost of all 4 links followed by a space

Video link : https://www.youtube.com/watch?v=eyKt5qtcBHM

The demo uses the route update time of 5 seconds for recording purposes but the actual code uses 1 second
for faster convergence.