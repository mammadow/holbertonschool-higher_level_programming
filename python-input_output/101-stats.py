#!/usr/bin/python3
"""
This script reads stdin line by line and computes metrics.
It prints statistics every 10 lines and upon keyboard interruption.
"""

import sys


def print_stats(total_size, status_counts):
    print("File size: {}".format(total_size))
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print("{}: {}".format(status, status_counts[status]))

total_size = 0
line_count = 0
status_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

try:
    for line in sys.stdin:
        parts = line.split()

        if len(parts) >= 2:
            status = parts[-2]
            size = parts[-1]

            if status in status_counts:
                status_counts[status] += 1

            try:
                total_size += int(size)
            except Exception:
                pass

        line_count += 1

        if line_count % 10 == 0:
            print_stats(total_size, status_counts)

except KeyboardInterrupt:
    print_stats(total_size, status_counts)
    raise
