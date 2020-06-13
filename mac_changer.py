#!/usr/bin/env python

import subprocess # call() function for shell commands
import optparse   # get values as arguments

# function that handles the user arguments
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC Address")
    parser.add_option("-m", "--mac", dest="mac_addr", help="New MAC Address")
    (options, arguments) = parser.parse_args()  # handles arguments keys and values
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.mac_addr:
        parser.error("[-] Please specify a new MAC Address, use --help for more info.")
    return options

# function that changes the MAC Address of selected interface
def change_mac(interface, mac_addr):
    print("[+] Changing MAC Address for " + interface + " to " + mac_addr)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_addr])
    subprocess.call(["ifconfig", interface, "up"])

options = get_arguments()
change_mac(options.interface, options.mac_addr)
