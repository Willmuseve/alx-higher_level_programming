#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body.
Python script that takes in a URL,
sends a request to the URL and displays the body of the response.
If the HTTP status code is greater than or equal to 400, print:
Error code: followed by the value of the HTTP status code
You must use the packages requests and sys
"""
import sys
import requests


if __name__ == "__main__":
    x = sys.argv[1]

    y = requests.get(x)
    if y.status_code >= 400:
        print("Error code: {}".format(y.status_code))
    else:
        print(y.text)
