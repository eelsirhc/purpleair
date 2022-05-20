import json
import requests

def get():
    config = json.load(open(".readkey",'r'))
    key = config["key"]

    url = "{api_url}?fields={fields}&show_only={station_id}".format(**config)
    headers = {'X-API-Key': key}
    response = requests.get(url, headers=headers)
    if response.ok:
        rj = response.json()
        json.dump(rj,open(snakemake.output[0],'w'))


get()
