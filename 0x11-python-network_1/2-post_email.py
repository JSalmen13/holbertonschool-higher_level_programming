#!/usr/bin/python3
"""script that fetches https://intranet.hbtn.io/status"""

from urllib import request, parse
from sys import argv

if __name__ == "__main__":
    data = parse.urlencode({"email": argv[2]}).encode('utf-8')
    with request.urlopen(argv[1], data) as page:
        print(page.read().decode('utf-8'))
