#!/usr/bin/python3
"""script that fetches https://intranet.hbtn.io/status"""

import requests
from sys import argv

if __name__ == "__main__":
    print(requests.post(argv[1], data={'email': argv[2]}).text)
