#!/usr/bin/python3
"""Script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""
import requests
import sys


if __name__ == "__main__":
    args = sys.argv
    if len(args) == 1:
        data = {"q": ""}
        print("No result")
    else:
        q = args[1]
        data = {"q": q}
        r = requests.post("http://0.0.0.0:5000/search_user", data)
        try:
            json_response = r.json()
            if json_response == {}:
                print("No result")
            else:
                print("[{}] {}".format(
                    json_response.get('id'),
                    json_response.get('name')))
        except ValueError:
            print("Not a valid JSON")
