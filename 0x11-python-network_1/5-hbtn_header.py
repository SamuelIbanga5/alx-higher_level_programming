#!/usr/bin/python3
"""Script that takes in a URL, sends a request to the URL and
displays the value of the variable X-Request-Id in the response header."""
import requests
import sys


if __name__ == "__main__":
    args = sys.argv
    url = args[1]
    r = requests.get(url)
    print(r.headers["X-Request-Id"])
