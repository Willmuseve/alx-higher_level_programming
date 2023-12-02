#!/usr/bin/python3

"""
a Python script that takes in a URL, sends a request to the URL and
displays the value of the variable X-Request-Id
use the packages requests and sys
"""

import sys
import requests


if __name__ == "__main__":
    link = sys.argv[1]

    response = requests.get(link)
    print(response.headers.get("X-Request-Id"))
