# coding=utf-8
class Record:
    __slots__ = "destination", "next_hop", "mask", "cost"

    def __init__(self, destination, next_hop, mask, cost):
        self.destination = destination
        self.next_hop = next_hop
        self.mask = mask
        self.cost = cost

    def set_destination(self, destination):
        self.destination = destination

    def set_next_hop(self, next_hop):
        self.next_hop = next_hop

    def set_mask(self, mask):
        self.mask = mask

    def set_cost(self, cost):
        self.cost = cost

    def get_network_addr(self):
        network = ""
        dest = self.destination.split(".")
        mask = self.mask.split(".")
        for index in range(len(dest)):
            network += str(int(dest[index]) & int(mask[index]))
            if index < len(dest) - 1:
                network += "."
        return network

    def __str__(self):
        return '{:25s} {:15s} {:15s} {:10s}'.format(
            str(self.get_network_addr()), str(self.mask), str(self.next_hop), str(self.cost))


def test():
    record = Record("25.80.20.30", "Unavailable", "255.255.255.0", 0)
    record2 = Record("25.80.20.196", "25.80.20.30", "255.255.255.0", 15)
    print(record)
    print(record2)