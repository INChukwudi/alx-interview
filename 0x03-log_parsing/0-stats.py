#!/usr/bin/python3

"""
Script that reads stdin line by line and computes metrics
"""

import re
import sys


ip_address_pattern = (
    r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.)'
    r'{3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
)
datetime_format_pattern = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}$'


def is_ip_format(address):
    """
    function that checks if the adress passed in conforms to
    a valid ip_address format
    """
    return re.match(ip_address_pattern, address) is not None


def is_datetime_format(date_string):
    """
    function that checks if the date strign passed in conforms to
    a valid datetime.now() output
    """
    return re.match(datetime_format_pattern, date_string[1:-1]) is not None


def print_metrics(metrics):
    """
    Function that prints out the metrics to the console
    """
    total_size = sum(metrics["file_sizes"])
    print("File size: {}".format(total_size))

    status_counts = metrics["status_counts"]
    for status_code in sorted(status_counts.keys()):
        count = status_counts[status_code]
        if count > 0:
            print("{}: {}".format(status_code, count))


def parse_metrics():
    """
    function that parses the metrics and coordinates printing to the console
    """
    metrics = {
        'file_sizes': [],
        'status_counts': {
            200: 0,
            301: 0,
            400: 0,
            401: 0,
            403: 0,
            404: 0,
            405: 0,
            500: 0
        }
    }

    try:
        line_count = 0
        for line in sys.stdin:
            line_count += 1
            parts = re.split(r'\s+', line.strip())

            date_string = parts[2] + " " + parts[3]
            if is_ip_format(parts[0]) and is_datetime_format(date_string):
                try:
                    status_code = int(parts[-2])
                    file_size = int(parts[-1])
                    if status_code in metrics["status_counts"]:
                        metrics["status_counts"][status_code] += 1
                    metrics["file_sizes"].append(file_size)
                except ValueError:
                    pass

            if line_count == 10:
                print_metrics(metrics)
                line_count = 0
    except KeyboardInterrupt:
        print_metrics(metrics)


if __name__ == "__main__":
    parse_metrics()
