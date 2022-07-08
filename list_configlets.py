#!/usr/bin/python3

from cvprac.cvp_client import CvpClient

# This disables the SSL certificate warning

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


cvp = '192.168.0.5'
cvp_user = 'arista'
cvp_passwd = 'aristasml8'

client = CvpClient()

client.connect([cvp], cvp_user, cvp_passwd)

inventory = client.api.get_inventory()

for item in inventory:
    print("Switchname:", item['hostname'])
    configet_list = client.api.get_configlets_by_device_id(item['key'], start=0, end=0)
    for configlet in configet_list:
        print("  Configlet: ", configlet['name'])


