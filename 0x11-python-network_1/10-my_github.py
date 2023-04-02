#!/usr/bin/python3
"""Script that takes your Github credentials (username and password)
 and uses the Github API to display your id."""
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":
    args = sys.argv
    username = args[1]
    password = args[2]
    basic = HTTPBasicAuth(username, password)
    r = requests.get('https://api.github.com/user', auth=basic)
    print(r.json().get("id"))
