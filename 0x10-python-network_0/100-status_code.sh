#!/usr/bin/bash
# A Bash script that sends a request to a URL passed as an argument, and displays 
curl -s -o /dev/null -w "%{http_code}" "$1"
