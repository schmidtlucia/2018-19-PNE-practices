import http.client
import termcolor
import json

import requests
import sys


server = "http://rest.ensembl.org"
ext = "/archive/id/ENSG00000165879?"  # ENSG00000157764 esto es el código para el FRA1 gene

r = requests.get(server + ext, headers={"Content-Type": "application/json"})

if not r.ok:
    r.raise_for_status()
    sys.exit()

decoded = r.json()

print(decoded)
