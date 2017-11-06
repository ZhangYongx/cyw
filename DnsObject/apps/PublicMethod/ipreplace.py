# -*- coding: utf-8 -*-
class IpReplace:
    ip = '11000000101'

    def __init__(self, strip):
        self.ip = strip

    def ch1(self):
        s = []
        for i in range(4):
            s.append(str(self.ip % 256))
            self.ip /= 256
        return '.'.join(s[::-1])

    def bintoip(self):
        self.ip = int(self.ip, 2)
        return self.ch1()