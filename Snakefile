import datetime
import glob

def generate_date():
    return datetime.datetime.now().strftime("%Y-%m-%d")

def generate_raw_time():
    return datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")

ruleorder: simulate > download

rule simulate:
    input:
        "sim.json"
    output:
        "raw_data/"+generate_raw_time()+".json"
    script:
        "scripts/save_to_json.py"

rule merge:
    input:
        glob.glob("raw_data/"+generate_date()+"*.json")
    output:
        "data/"+generate_date()+".csv"
    script:
        "scripts/write_to_csv.py"

rule download:
    output:
        "raw_data/"+generate_raw_time()+".json"
    script:
        "scripts/download_to_json.py"

#rule download:
#    input:
#        "raw_data/"+generate_raw_time()+".json"
