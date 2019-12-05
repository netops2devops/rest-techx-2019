# Objective : To extract AS-NAME for a given ASN

import requests 
import json
from pprint import pprint

# Request server to send JSON formatted output
response = requests.get("https://whois.arin.net/rest/asn/AS1224.json")

# RESPONSE OUTPUT
print("-- JSON based output --\n")
print(response.text)
print("")
print("Ew! WHAT A MESS!")
