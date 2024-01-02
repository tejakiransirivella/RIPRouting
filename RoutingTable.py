# coding=utf-8
class RoutingTable:
    __slots__ = "records"

    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def __str__(self):
        output = "=================================================================\n"
        output += '{:25s} {:15s} {:15s} {:10s}\n'. \
            format("Destination Ip Address", "Subnet Mask", "Next Hop", "Distance")
        output += "=================================================================\n"
        for record in self.records:
            output += str(record) + "\n"
        output += "=================================================================\n"
        return output
