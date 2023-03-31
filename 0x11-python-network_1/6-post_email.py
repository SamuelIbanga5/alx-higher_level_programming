#!/usr/bin/python3
"""Script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter
and finally displays the body of the response."""
import requests
import sys


if __name__ == "__main__":
    args = sys.argv
    url = args[1]
    email = args[2]
    data = {"email": email}
    r = requests.post(url, data)
    print(r.text)
