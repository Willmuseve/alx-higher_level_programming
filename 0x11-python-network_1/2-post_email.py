#!/usr/bin/python3
"""
a Python script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays the body
of the response (decoded in utf-8)
"""
from urllib import request, parse
from sys import argv

if __name__ == "__main__":
    link = argv[1]
    value = {"email": argv[2]}
    info = parse.urlencode(value).encode()
    with request.urlopen(request.Request(link, info)) as response:
        print(response.read().decode("utf-8"))
