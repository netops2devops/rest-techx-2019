# Goal : To extract AS-NAME for ANY given ASN

import requests
import json
import sys

def GetASName(asn):
    response = requests.get("https://whois.arin.net/rest/asn/AS{0}.json".format(asn))
    data = json.loads(response.text)

    asnum = data['asn']['endAsNumber']['$']
    asname = data['asn']['orgRef']['@name']
    
    #Formatted output
    print("{0} => {1}".format(asnum, asname))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Invalid arguments")
        exit()

    else:
        GetASName(sys.argv[1])


