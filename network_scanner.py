#!/usr/bin/env python3

import scapy.all as scapy
import argparse

def ip():
    parse = argparse.ArgumentParser()
    parse.add_argument("-ip", dest="ip", help="Needs IP range /24")
    options= parse.parse_args()
    return options


def scan(ip):
    arp_request = scapy.ARP(pdst = ip)
    broadcast= scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    ans,unans= scapy.srp(arp_request_broadcast, timeout=1)
    print(ans.summary())


options = ip()
scan(options.ip)
