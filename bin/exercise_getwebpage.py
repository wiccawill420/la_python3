#!/home/cloud_user/venvs/experiment/bin/python3

import os
import requests
import sys
import json
from argparse import ArgumentParser

parser = ArgumentParser(description="downloads given webpage to a file")
parser.add_argument('webpage', help='the full url to download')
parser.add_argument('outfile', help='where to save the downloaded page')
parser.add_argument('--mode', default='html', help='set output mode as json or html, default is html')
args = parser.parse_args()

if args.mode not in ['json','html']:
    print("Error: output mode must be json or html")
    sys.exit(1)

res = requests.get(args.webpage)

if res.status_code != 200:
    print(f"Error connecting: {args.webpage} returned status {res.status_code}")
    sys.exit(1)
if args.mode == 'json':
    try:
        content = json.dumps(res.json())
    except ValueError:
        print("Error: Content is not JSON")
        sys.exit(1)
else:
    content = res.text

with open(args.outfile, 'w') as f:
    f.write(content)
    print(f"Content written to '{args.outfile}'")

