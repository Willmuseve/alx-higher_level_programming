#!/usr/bin/python3
"""Python script
"""
import sys
import requests


if __name__ == "__main__":
    l = "" if len(sys.argv) == 1 else sys.argv[1]
    d = {"q": l}

    n = requests.post("http://0.0.0.0:5000/search_user", data = d)
    try:
        response = n.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
