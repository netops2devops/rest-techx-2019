#!/usr/bin/env python3

import requests
import json
import sys
from pprint import pprint
from random import randint


def GetASName(asn_list):
    mapping = dict()

    for asn in asn_list:
        response = requests.get(
            "https://whois.arin.net/rest/asn/AS{0}.json".format(asn)
        )
        data = json.loads(response.text)

        # Extract ASN and AS-NAME from data loaded as a dictionary
        asnum = data["asn"]["endAsNumber"]["$"]
        asname = data["asn"]["orgRef"]["@name"]

        # Dictionary to store ASN <=> AS-NAME mapping
        mapping[asnum] = asname

    # Returns a dictionary when function is called
    return mapping


def push2netbox(mapping):

    # Do NOT use plain-text-auth-tokens in production ; either use the getpass library or Vault to store tokens and credentials
    headers = {
        "Authorization": "Token 2cf8f987c1361e672a8ec947b5bd40a9b5716e40",
        "Content-Type": "application/json",
    }

    for asnum, asname in mapping.items():
        info = {
            "name": asname,
            "asn": asnum,
            "slug": randint(1, 100000),
            "description": "peering point",
        }
        data = json.dumps(info)

        # Create new site with extracted ASN and ASNAME
        response = requests.post(
            "http://0.0.0.0:32768/api/dcim/sites/",
            data=data,
            headers=headers,
            verify=False,
        ).json()
        pprint(response)
        print("\n")

        # Next steps :
        # Create circuit type BGP peering
        # Add A-Z end points of a circuit


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Requires atleast one arguments as ASN")
        exit()

    else:
        # List of ASN's in arguments
        asn_list = sys.argv[1:]

        # Function call
        asn2name = GetASName(asn_list)
        push2netbox(asn2name)
