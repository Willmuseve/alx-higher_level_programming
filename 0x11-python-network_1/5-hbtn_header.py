#!/usr/bin/python3
"""A Python script that takes in a URL,
sends a request to the URL and displays
the value of the variable X-Request-Id in the response header
Used package requests and sys

"""
import sys
import requests


if __name__ == "__main__":
    x = sys.argv[1]

    y = requests.get(x)
    print(y.headers.get("X-Request-Id"))
