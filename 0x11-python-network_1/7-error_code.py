#!/usr/bin/python3
"""Script that takes in a URL, send a request to the URL
and displays the body of the response."""
import requests
import sys


if __name__ == "__main__":
    args = sys.argv
    url = args[1]
    status_code = requests.get(url).status_code
    if status_code >= 400:
        print("Error code: {}".format(status_code))
