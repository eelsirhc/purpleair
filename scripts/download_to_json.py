import json
import requests
from pathlib import Path


def get(config, output_filename):

    url = "{api_url}?fields={fields}&show_only={station_id}".format(**config)
    headers = {'X-API-Key': config["key"]}
    response = requests.get(url, headers=headers)
    if response.ok:
        rj = response.json()
        output_filename.parent.mkdir(parents=True, exist_ok=True)
        json.dump(rj,open(output_filename,'w'))

if __name__ == "__main__":
    try:
        output_filename = snakemake.output[0]
    except NameError:
        import sys
        output_filename = sys.argv[1] # first argument
        output_filename = Path(output_filename)

    config = json.load(open(".readkey",'r'))
    #config is a dictionary containing
    # key -> the key id
    # station_id -> the station id
    # fields -> fields to download
    # api_url -> the url to access
    
    get(config, output_filename)
