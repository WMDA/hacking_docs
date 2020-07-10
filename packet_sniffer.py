import scapy.all as scapy
from scapy.layers import http
import argparse

def options():
    parse = argparse.ArgumentParser()
    parse.add_argument('-i','--interface',dest='interface',help='Needs interface')
    options= parse.parse_args()
    if not options.interface:
        parse.error('Specify interface using -i')
    else:
        return options


def sniffer(interface):
    scapy.sniff(iface=interface, store=False, prn=processer)

def processer(packet):
    if packet.haslayer(http.HTTPRequest):
        print(packet)
        
options=options()
sniffer(options.interface)
