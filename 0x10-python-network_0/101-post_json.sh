#!/bin/bash
# A bash script that sends a JSON POST request to a URL, and displays
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
