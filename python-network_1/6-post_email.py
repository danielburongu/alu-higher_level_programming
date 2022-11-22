#!/usr/bin/python3
"""takes url and display the body of the response"""


import requests
import sys


if __name__ == "__main__":
    """sending the variable email"""
    url = sys.argv[1]
    email = sys.argv[2]
    context = {
        "email": email
    }
    reply = requests.post(url, data=context)
    print("{}".format(reply.text))
