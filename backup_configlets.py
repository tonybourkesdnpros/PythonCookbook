
from cvprac.cvp_client import CvpClient
import requests
import os
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

cvp = "192.168.0.5"
cvp_user = "arista"
cvp_pw = "aristakysb"

client = CvpClient()

client.connect([cvp], cvp_user, cvp_pw)

directory = "configs"
exists = os.path.exists(directory)
if not exists:
    os.makedirs(directory)


configlets = client.api.get_configlets(start=0,end=0)

for item in configlets['data']:
    file = open(directory+'/'+item['name']+'.txt','w')
    file.write(item['config'])
    file.close()
