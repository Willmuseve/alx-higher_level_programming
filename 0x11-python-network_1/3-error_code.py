#!/usr/bin/python3
"""Python script that takes in a URL,
sends a request to the URL and displays the body
of the response.
manage urllib.error.HTTPError exceptions and print:
Error code: followed by the HTTP status code
"""
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":

    x = sys.argv[1]

    request = urllib.request.Request(x)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
