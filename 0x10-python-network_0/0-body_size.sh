#!/usr/bin/env bash
# Bash script that takes in a URL, sends a request to that URL and displays the size of the body of the response
curl -s --write-out '%{size_download}\n' 0.0.0.0:5000 | tr -d "Index page"
