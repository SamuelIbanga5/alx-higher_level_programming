#!/usr/bin/python3
"""Script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""
import requests
import sys


if __name__ == "__main__":
    args = sys.argv
    if len(args) == 1:
        q = ""
    else:
        q = args[1]
        data = {"q": q}
        r = requests.post("http://0.0.0.0:5000/search_user", data)
        print(r.text)
