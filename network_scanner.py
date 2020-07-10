#!/usr/bin/env python3

import scapy.all as scapy
import argparse
from datetime import datetime
import sys

def ip():
    parse = argparse.ArgumentParser()
    parse.add_argument("-ip", dest="ip", help="Needs IP range /24")
    parse.add_argument("-i", dest="interface", help='Needs interface')
    options= parse.parse_args()
    if not options.ip:
        parse.error('>> Needs ip address. Use -h for further details.')
    elif not options.interface:
        parse.error('>> Needs interface. Use -h for further details')
    else:
        return options


def scan(ip,interface):
    arp_request = scapy.ARP(pdst = ip)
    broadcast= scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    ans = scapy.srp(arp_request_broadcast, timeout=1,iface=interface, verbose=False)[0]
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
try:
    print('\nScanning please wait:\n ')
    start=datetime.now()
    scan_results=scan(options.ip, options.interface)
    stop=datetime.now()
    duration= stop-start
    output(scan_results)
    print('-'*100,'\nScan Complete\n')
    print('Scan duration: %s'%(duration))
except KeyboardInterrupt:
    print('User requested shut down:')
    sys.exit()
