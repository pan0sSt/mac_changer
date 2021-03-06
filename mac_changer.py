#!/usr/bin/env python

import subprocess # run() function for shell commands
import argparse   # get values as arguments
import re         # regural expressions

# function that handles the user arguments
def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", help="Interface to change its MAC Address") # eth0
    parser.add_argument("-m", "--mac", dest="mac_addr", help="New MAC Address") # 08:00:27:23:ff:90
    options = parser.parse_args()  # handles arguments keys and values
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.mac_addr:
        parser.error("[-] Please specify a new MAC Address, use --help for more info.")
    return options

# function that changes the MAC Address of selected interface
def change_mac(interface, mac_addr):
    print("[+] Changing MAC Address for " + interface + " to " + mac_addr)
    subprocess.run(["ifconfig", interface, "down"])
    subprocess.run(["ifconfig", interface, "hw", "ether", mac_addr])
    subprocess.run(["ifconfig", interface, "up"])

# function that returns the MAC Address of selected interface
def get_curr_mac(interface):
    ifconfig_result = subprocess.run(["ifconfig", interface], capture_output=True, text=True).stdout
    mac_addr_search_result = re.search(r"(\w\w:){5}\w\w", ifconfig_result)
    if mac_addr_search_result:
        return mac_addr_search_result.group(0)
    else:
        print("[-] Could not read MAC Address.")

options = get_arguments()

curr_mac = get_curr_mac(options.interface)
print("Current MAC = " + str(curr_mac))

change_mac(options.interface, options.mac_addr)

curr_mac = get_curr_mac(options.interface)
if curr_mac == options.mac_addr:
    print("[+] MAC Address was successfully changed to " + curr_mac)
else:
    print("[-] MAC Address did not change")
