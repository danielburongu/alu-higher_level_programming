#!/usr/bin/python3
'''use github api to know me'''

import requests
import sys
import requests.auth

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    basic = requests.auth.HTTPBasicAuth(username, password)
    response = requests.get(
        'https://api.github.com/user', auth=basic)
    try:
        json_response = response.json()
        print("{}".format(json_response["id"]))
    except:
        print(None)