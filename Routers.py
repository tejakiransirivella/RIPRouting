# coding=utf-8
class Routers:
    __slots__ = "routers"

    def __init__(self):
        self.routers = {}

    def add_routing_table(self, address, routing_table):
        self.routers[address] = routing_table

    def get_routing_table(self, address):
        return self.routers[address]

    def __str__(self):
        output = ""
        for key in self.routers.keys():
            output += key + "\n" + str(self.routers[key])
        return output
