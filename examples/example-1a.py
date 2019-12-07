# objective : To extract AS-NAME for any given ASN
# This script pulls info from whois records for ASN 1224

import requests

response = requests.get("https://whois.arin.net/rest/asn/AS1224")
print(response.text)
print()
print('WHAT A MESS')
