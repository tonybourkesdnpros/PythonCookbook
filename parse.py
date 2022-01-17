#!/usr/bin/python3

import json

file = open('response.json', 'r')

output = json.load(file)

for interface in output['result'][0]['interfaces']:
    ip = output['result'][0]['interfaces'][interface]['interfaceAddress']['ipAddr']['address']
    mask = output['result'][0]['interfaces'][interface]['interfaceAddress']['ipAddr']['maskLen']
    print("interface", interface)
    print("  ip address", str(ip) + "/" + str(mask))

