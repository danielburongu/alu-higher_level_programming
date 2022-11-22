#!/usr/bin/python3
"""take a url and display the values"""


import requests
import sys


if __name__ == "__main__":
    """send the email"""
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code <= 400:
        print("{}".format(response.text))
    else:
        print("Error code: {}".format(response.status_code))