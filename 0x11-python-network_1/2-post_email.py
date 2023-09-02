#!/usr/bin/python3
""" A Python script that takes in a URL and an email,
sends a POST request to the passed
URL with the email as a parameter, and
displays the body of the response
urllib and sys packages used
email sent in the email variable
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    x = sys.argv[1]
    a = {"email": sys.argv[2]}
    b = urllib.parse.urlencode(a).encode("ascii")

    request = urllib.request.Request(x, b)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
