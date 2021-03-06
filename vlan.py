#!/usr/bin/python3

import pyeapi

connect = pyeapi.connect_to('OOB-DC1')

# Opens a file in read-only
file = open('list.vlan', 'r')

# Converts raw file read to text string
vlan_list = file.readlines()

# Loop through VLAN list
for vlan_id in vlan_list: 
    result = connect.api("vlans").delete(vlan_id)

# Result is only a Boolean, it doesn't include any details of success or failure
    if result == True:
        print("Successfully deleted VLAN", vlan_id)

    if result == False:
        print("Failure")


