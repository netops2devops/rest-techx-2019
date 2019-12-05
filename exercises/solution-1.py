#!/usr/bin/env python3

# Modify example-1e.py to print ASN <=> AS-NAME mapping for a list of AS numbers as a dictionary
# example : your input should look something like this
# ./exercise-1.py 1224 38 19782 1767 14877

import requests
import json
import sys

def GetASName(asn_list):

    for asn in asn_list:
        response = requests.get("https://whois.arin.net/rest/asn/AS{0}.json".format(asn))
        data = json.loads(response.text)

        # Extract ASN and AS-NAME from data loaded as a dictionary
        asnum = data['asn']['endAsNumber']['$'] 
        asname = data['asn']['orgRef']['@name']

        # Dictionary to store ASN <=> AS-NAME mapping
        mapping[asnum]=asname
    
    print(mapping)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Requires two or more arguments")
        exit()

    else:
        # Dictionary to store ASN <=> AS-NAME mapping
        mapping = dict()
        
        # List of ASN's in arguments
        asn_list = sys.argv[1:]
        
        # Function call 
        GetASName(asn_list)
