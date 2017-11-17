# -*- coding: utf-8 -*-
# Author: zhangx
import re
from IPy import IP


# 点分十进制转二进制
def ip_int2bin(ip):
    return IP(ip).strBin()


# 二进制转点分十进制
def ip_bin2int(ip):
    return ".".join([str(int(i, 2)) for i in re.findall(r'.{8}', ip)])
