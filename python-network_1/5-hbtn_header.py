#!/usr/bin/python3
"""sends a request to the url and displays value in response header"""


import requests
import sys


if __name__ == "__main__":
    """shows value of variable"""
    url = sys.argv[1]
    reply = requests.get(url)
    print("{}".format(reply.headers.get('X-Request-Id')))
