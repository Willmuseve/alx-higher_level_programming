#!/usr/bin/python3
"""
A Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""
if __name__ == "__main__":
    import requests
    import sys

    x = "https://api.github.com/user"
    u = sys.argv[1]
    p = sys.argv[2]
    dx = requests.get(x, auth=(u, p))

    try:
        d = dx.json()
        print(d["id"])
    except Exception:
        print("None")
