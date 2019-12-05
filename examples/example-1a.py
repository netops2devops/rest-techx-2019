import requests

response = requests.get("https://whois.arin.net/rest/asn/AS1224")

print(response)
print(response.text)
