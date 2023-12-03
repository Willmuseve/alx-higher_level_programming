#!/bin/bash
# A script that uses curl to send a request
curl -s "$1" | wc -c
