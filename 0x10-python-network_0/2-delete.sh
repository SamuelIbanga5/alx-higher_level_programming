#!/bin/bash
# Script that sends a DELETE request to the URL passd as an argument and displays the body of the response.
curl -s -X delete "$1"
