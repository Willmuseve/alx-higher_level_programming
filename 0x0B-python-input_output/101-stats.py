#!/usr/bin/python3
"""
does the reading of stdin line by line
"""
import sys

file_size = 0
status_tally = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
y = 0
try:
    for line in sys.stdin:
        tokens = line.split()
        if len(tokens) >= 2:
            a = y
            if tokens[-2] in status_tally:
                status_tally[tokens[-2]] += 1
                y += 1
            try:
                file_size += int(tokens[-1])
                if a == y:
                    y += 1
            except FileNotFoundError:
                if a == y:
                    continue
        if i % 10 == 0:
            print("File size: {:d}".format(file_size))
            for key, value in sorted(status_tally.items()):
                if value:
                    print("{:s}: {:d}".format(key, value))
    print("File size: {:d}".format(file_size))
    for key, value in sorted(status_tally.items()):
        if value:
            print("{:s}: {:d}".format(key, value))

except KeyboardInterrupt:
    print("File size: {:d}".format(file_size))
    for key, value in sorted(status_tally.items()):
        if value:
            print("{:s}: {:d}".format(key, value))
