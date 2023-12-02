#!/usr/bin/python3

"""
a Python script that fetches https://alx-intranet.hbtn.io/status
use the package requests
"""

import requests


if __name__ == "__main__":
    respons = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(respons.text)))
    print("\t- content: {}".format(respons.text))
