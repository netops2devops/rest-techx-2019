import requests

response = requests.get("https://whois.arin.net/rest/asn/AS1224")
print(response.text)
print()
print('WHAT A MESS')
