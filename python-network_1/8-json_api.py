#!/usr/bin/python3
"""send letter"""
import requests
import sys

if __name__ == '__main__':
    try:
        lett = sys.argv[1]
    except IndexError:
        lett = ""
    response = requests.post(
        "http://0.0.0.0:5000/search_user",
        data={"q": lett}
    )
    try:
        json_response = response.json()
        if response.headers.get("Content-Type") == 'application/json':
            if len(json_response) > 0:
                print("[{}] {}".format(
                    json_response["id"],
                    json_response["name"])
                )
            else:
                print("No result")
    except:
        print("Not a valid JSON")