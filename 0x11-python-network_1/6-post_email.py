#!/usr/bin/python3
""" Sending a POST request with the email as parameter """

if __name__ == "__main__":
    import requests
    import sys

    link = sys.argv[1]
    email = sys.argv[2]
    data = requests.post(link, {"email": email})

    print(data.text)
