# RouterCommunication

This project implements a distance-vector routing protocol called RIP.

## Prerequisites

- Python version 2.7.18

## Project Structure

- **ServerClient:** Main program that initializes both server (receives route updates) and client (sends route updates).
- **RouterClient:** Handles the client side of the program, sending route updates to its neighbors.
- **RouterServer:** Handles the server side of the program, receiving route updates from its neighbors and updating the routing tables if the route is optimal.
- **RouterTopology:** Creates a topology and generates routing tables for a router based on the topology.
- **Routers, RoutingTable, Record:** These are classes that store routing table information and print them.

## Program Execution

Execute `ServerClient.py` on all router machines and provide the cost of all 4 links, followed by a space.

## Demo Video

[Watch the demo video](https://www.youtube.com/watch?v=eyKt5qtcBHM)

The demo uses a route update time of 5 seconds for recording purposes, but the actual code uses 1 second for faster convergence.
