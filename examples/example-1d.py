# Goal : To extract AS-NAME for a given ASN

import requests
import json

response = requests.get("https://whois.arin.net/rest/asn/AS1224.json")
data = json.loads(response.text)
formatted_data = json.dumps(data, indent=4, sort_keys=True) 

#Formatted output
print(data['asn']['endAsNumber']['$'] + " =>\t" + data['asn']['orgRef']['@name'])
