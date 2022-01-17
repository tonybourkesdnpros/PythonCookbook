#!/usr/bin/python3

import pyeapi

connect = pyeapi.connect_to('OOB-DC1')

# Opens a file in read-only
file = open('list.vlan', 'r')

vlan_list = file.readlines()

for vlan_id in vlan_list: 
    result = connect.api("vlans").delete(vlan_id)

    if result == True:
        print("Successfully deleted VLAN", vlan_id)

    if result == False:
        print("Failure")


