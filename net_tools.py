#! /usr/bin/env python

from __future__ import print_function
from scapy.all import ARP, sr

class HWAddrError(Exception):
    """Error getting hardware address."""
    pass

def get_hwaddr(ip):
    """
    Get hardware address from IP

    ip -- IP of target device (e.g. '192.168.1.1')
    """
    if not ip:
        raise HWAddrError('ip argument is None')

    r, u = sr(ARP(op=ARP.who_has, pdst=ip), timeout=1, verbose=False)
    
    if r.res:
        return r.res[0][1][ARP].hwsrc
    else:
        raise HWAddrError('Error getting hardware address.')

if __name__ == "__main__":
    print(get_hwaddr('192.168.1.103'))
