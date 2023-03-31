#!/usr/bin/python3
"""Script that takes in a URL, send a request to the URL
and displays the body of the response (decoded in utf-8)."""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    args = sys.argv
    url = args[1]
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
