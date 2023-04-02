#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL and displays the size of the body of the response
curl -s "$1" --write-out '%{size_download}\n' 0.0.0.0:5000 | cut -c 11- | uniq -d
