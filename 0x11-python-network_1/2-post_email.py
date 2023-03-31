#!/usr/bin/python3
"""Script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter
and displays the body of the response (decoded in utf-8)."""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    args = sys.argv
    url = args[1]
    email = args[2]
    value = {"email": email}
    data = urllib.parse.urlencode(value).encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print("Your email is: {}".format(body))
