#!/bin/bash
# Script that sends a JSON post request to a URL Passwd as the first argument, displays the body of the response.
curl -sL -H "content-type:application/json" -d @"$2" -X POST "$1"
