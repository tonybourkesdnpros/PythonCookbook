#/usr/bin/python3

from cvprac.cvp_client import CvpClient
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

cvp1 = "192.168.0.5"
cvp_user = "arista"
cvp_pw = "aristaox5o" # Change this to your environment password


client = CvpClient()

client.connect([cvp1], cvp_user, cvp_pw)

inventory = client.api.get_inventory()

print("Looping through individual devices:")

for item in inventory:
    device = item['hostname']
    device_dict = client.api.get_device_by_name(device, search_by_hostname=True)

    base = device+'-BASE'
    base_configlet = client.api.get_configlet_by_name(base)
    base_configlet_list = [base_configlet]
    device_key = device_dict['key']
    device_configlets = client.api.get_configlets_by_device_id(device_key)
    for configlet in device_configlets:
        #print(configlet)
        configlet_name = configlet['name']
        configlet_list_item = [configlet]
        # print(configlet_list_item)
        base = device+'-BASE'
        if ('ATD-INFRA' not in configlet_name) and (base not in configlet_name):
            print("Deleting", configlet_name, "from", device)
            client.api.remove_configlets_from_device('Cleanup script', item, configlet_list_item, create_task=True)
    #print("Making sure", configlet_list_item, "is applied")
    base_item = [base]
#    print(base)
   
    client.api.apply_configlets_to_device('Cleanup script', item, base_configlet_list, create_task=True, reorder_configlets=False)

print("Starting looping through containers")
containers = client.api.get_containers()
for container in containers['data']:
    #print("Container", container['name'])
    applied_configlets_to_container = client.api.get_configlets_by_container_id(container['key'])
    for applied_to_container in applied_configlets_to_container['configletList']:
        print("Container", container['name'], "has container", applied_to_container['name'], "applied,")
        if applied_to_container['name'] != 'ATD-INFRA':
            list_of = [applied_to_container]
            client.api.remove_configlets_from_container('Cleanup script', container, list_of, create_task=True)
            print("Removing", applied_to_container['name'], "from", container['name'])
