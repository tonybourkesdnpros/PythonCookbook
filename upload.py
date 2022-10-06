from cvprac.cvp_client import CvpClient

# This makes the warnings for self-signed certificates go away
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

cvp = "192.168.0.5"
cvp_user = "arista"
cvp_passwd = "aristaxut9"

client = CvpClient()

client.connect([cvp], cvp_user, cvp_passwd)


configlet_name = "test"
config = "alias tonyb show ip interface brief"

client.api.add_configlet(configlet_name, config)
