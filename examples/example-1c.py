# Objective : To extract AS-NAME for a given ASN

import requests
import json
from pprint import pprint

# Request server to send JSON formatted output
response = requests.get("https://whois.arin.net/rest/asn/AS1224.json")

# LOAD response output as JSON | Serialize to give make it look more readable
data = json.loads(response.text)
json_data = json.dumps(data, indent=4, sort_keys=True)

print("-- JSON formatted readable output --\n")
print(json_data)
