#!/usr/bin/python3
""" A script that takes in a URL, sends a request to the
    URL and displays the value of the X-Request-Id """

from urllib.request import urlopen
from sys import argv

if __name__ == "__main__":
    link = argv[1]
    with urlopen(link) as response:
        header = response.getheader("X-Request-Id")
    print(header)
