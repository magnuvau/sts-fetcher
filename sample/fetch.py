from string import Template
from base64 import b64encode
from requests.auth import HTTPBasicAuth
import argparse
import requests
import json

hostnames = {}
creds = {}

with open('config/hostnames.config', 'r') as hostname_config:
    lines = hostname_config.readlines()
    for line in lines:
        line = line.strip('\n')

        # Ignore comments
        if ('#' in line or len(line) == 0):
            continue

        split_line = line.split(';')
        hostnames[split_line[0]] = split_line[1]

with open('config/creds.config', 'r') as creds_config:
    lines = creds_config.readlines()
    for line in lines:
        line = line.strip('\n')

        # Ignore comments
        if ('#' in line or len(line) == 0):
            continue

        split_line = line.split(';')
        creds[split_line[0]] = (split_line[1], split_line[2])

#print(URL.substitute(STS_URL="lol"))

parser = argparse.ArgumentParser(description='Fetch STS token.')
parser.add_argument('host', help='Name of which STS to use.')
parser.add_argument('creds', help='Name of credentials to use.')
args = parser.parse_args()

try:
    HOSTNAME=hostnames[args.host]
except KeyError:
    print("ERROR: STS \'%s\' not configured in config/hostnames.config" % args.host)
    exit

try:
    USERNAME=creds[args.creds][0]
    PASSWORD=creds[args.creds][1]
    CREDS="%s:%s" % (USERNAME, PASSWORD)
except KeyError:
    print("ERROR: Credentials \'%s\' not configured in config/creds.config" % args.creds)
    exit

url = "https://%s/rest/v1/sts/token?grant_type=client_credentials&scope=openid" % HOSTNAME
headers = {
    "Accept": "application/json"
}

request = requests.post(url, headers=headers, auth=HTTPBasicAuth(USERNAME, PASSWORD))
print(request.content)

