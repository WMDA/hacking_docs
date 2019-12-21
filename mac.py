#!/usr/bin/env python3

import subprocess
import argparse
import random

def mac_generator():
    mac_address = "02:%02x:%02X:%02x:%02x:%02x" % (random.randint(0, 255),random.randint(0, 255),
    random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
    return(mac_address)

def get_arguments():
    parse = argparse.ArgumentParser()
    parse.add_argument("-i", "--interface", dest='interface', required=True, help='Interface to change mac address.')
    parse.add_argument("-m","--mac", dest='mac',help='New mac address, can use --r to generate random.')
    parse.add_argument("-r", help='Randomly assigns mac address.', action='store_true')
    options= parse.parse_args()
    if options.r:
        options.mac = mac_generator()
    if not options.interface:
        parse.error(">> Needs interace. Use --help for more information.")
    elif not options.mac:
        parse.error(">> Needs mac address. Use --help for more information.")
    else:
        return options

def change_mac (interface, mac):
    print (">> changing: " + interface + " to " + mac )
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw","ether", mac])
    subprocess.call(["ifconfig", interface, "up"])
options = get_arguments()
change_mac(options.interface, options.mac)
