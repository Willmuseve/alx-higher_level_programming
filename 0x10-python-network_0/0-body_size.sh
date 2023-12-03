#!/bin/bash
# A script that uses curl to send a request to a
# cURL provided as arg and displays size of the body of the response
curl -s "$1" | wc -c
