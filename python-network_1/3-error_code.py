#!/usr/bin/python3
"""displays responses"""

import urllib.request
import urllib.error
import sys

if __name__ == '__main__':
    """"sends request"""
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as reply:
            data = reply.read()
            print("{}".format(data.decode("utf-8")))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
    except urllib.error.URLError as errr:
        print(errr.reason)
