#!/usr/bin/env python3

import subprocess
import argparse

def get_arguments():
    parse = argparse.ArgumentParser()
    parse.add_argument("-i", "--interface", dest='interface', help='Interface to change mac address')
    parse.add_argument("-m","--mac", dest='mac',help='New mac address')
    options= parse.parse_args()
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
