#!/usr/bin/python3
"""take a url and display the values"""


import requests
import sys


if __name__ == "__main__":
    """send the email"""
    url = sys.argv[1]
    email = sys.argv[2]
    context = {
        "email": email
    }
    response = requests.post(url, data=context)
    print("{}".format(response.text))