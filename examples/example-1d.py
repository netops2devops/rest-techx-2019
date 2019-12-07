# Goal : To extract AS-NAME for a given ASN

import requests
import json

response = requests.get("https://whois.arin.net/rest/asn/AS1224.json")
data = json.loads(response.text)
formatted_data = json.dumps(data, indent=4, sort_keys=True) 

# Extracting relevant data and storing in variables
asnum = data['asn']['endAsNumber']['$']
asname = data['asn']['orgRef']['@name']

print("{0} => {1}".format(asnum, asname))
