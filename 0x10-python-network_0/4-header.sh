#!/bin/bash
# Script that takes in a URL as an argument, sendsa GET request to the URL and displays the body of the response.
curl -sH "X-School-User-Id: 98" "$1"
