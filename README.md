# sts-fetcher

Enkelt python script for å hente ned NAV STS tokens.
## Setup
```bash
mkdir config
touch config/creds.config
touch config/hostnames.config
``` 
I _creds.config_ legg inn credentials, for eksempel:
```bash
test-creds;brukernavn;passord
``` 
I _hostnames.config_ legg inn URL, for eksempel:
```bash
test-sts-url;test-sts.example.com
``` 
## Eksempel
```bash
python3 sample/fetch.py test-creds test-sts-url
```
## Help
```bash
python3 sample/fetch.py -h
``` 