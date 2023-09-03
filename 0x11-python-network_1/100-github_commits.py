#!/usr/bin/python3
"""A python script that takes 2 arguments in order to solve this challenge.
The first argument will be the repository name
The second argument will be the owner name
You must use the packages requests and sys
"""
import sys
import requests


if __name__ == "__main__":
    x = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    n = requests.get(x)
    m = n.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                m[i].get("sha"),
                m[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
