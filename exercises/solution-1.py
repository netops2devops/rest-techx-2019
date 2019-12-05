# Modify example-1e.py to print ASN <=> AS-NAME mapping for a list of AS numbers
# example : your input should look something like this
# ./exercise-1.py 1224 38 19782 1767

import requests
import json
import sys

def GetASName(asn):
    response = requests.get("https://whois.arin.net/rest/asn/AS{0}.json".format(asn))
    data = json.loads(response.text)

    #Formatted output
    print(data['asn']['endAsNumber']['$'] + " =>\t" + data['asn']['orgRef']['@name'])

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Invalid number of arguments")
        exit()

    else:
        for asn in sys.argv[1:] :
            GetASName((asn))
