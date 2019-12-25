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
    ans = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    client_list=[]
    for i in ans:
        client_dic={'IP':i[1].psrc, 'MAC':i[1].hwsrc}
        client_list.append(client_dic)
    return client_list

def output(results_list):
    print('','-'*100,'\n',"\t IP \t\t\tMac address",'\n','-'*100)
    for i in results_list:
        print('\t',i['IP'] + "\t\t" + i['MAC'])

options = ip()
scan_results=scan(options.ip)
output(scan_results)
