# Goal : To extract AS-NAME for ANY given ASN

import requests
import json
import sys

def GetASName(asn):
    response = requests.get("https://whois.arin.net/rest/asn/AS{0}.json".format(asn))
    data = json.loads(response.text)

    #Formatted output
    print(data['asn']['endAsNumber']['$'] + " =>\t" + data['asn']['orgRef']['@name'])

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Invalid arguments")
        exit()

    else:
        GetASName(sys.argv[1])


