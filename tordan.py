from elasticsearch import Elasticsearch
import requests
from datetime import datetime

es = Elasticsearch(['http://splunkzeralab.brazilsouth.cloudapp.azure.com:9500'], http_auth=('elastic', 'V8uQBIQdYhqTtK2Oqww9'))
# es = Elasticsearch(['http://localhost:9500'], http_auth=('elastic', 'V8uQBIQdYhqTtK2Oqww9'))

response = requests.get("https://www.dan.me.uk/torlist/", verify=False)
i = 1
if response.status_code == 200:
    for ip in response.text.splitlines():
        es.index(index='idx_tordan', doc_type='ip', id=i, body={"reported_date": str(datetime.now()), "ip":ip})
        i=i+1

response = requests.get("https://talos-intelligence-site.s3.amazonaws.com/production/document_files/files/000/090/570/original/ip_filter.blf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIXACIED2SPMSC7GA%2F20200323%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20200323T011614Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=2a6cafa63408a9be97a3d3bc8b03e469e04c750cd339e7e1901ccdbf2244c261", verify=False)
print(response.status_code)

i = 1
if response.status_code == 200:
    for ip in response.text.splitlines():
        es.index(index='idx_ciscoblocklist', doc_type='ip', id=i, body={"reported_date": str(datetime.now()), "ip":ip})
        i=i+1