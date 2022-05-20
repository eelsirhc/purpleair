import pandas as pd
import json

def read_json(filename):
   js = json.load(open(filename,'r'))
   data = dict()
   data.update(dict(zip(js["fields"],js["data"][0])))
   for k in ["api_version", "time_stamp", "data_time_stamp"]:
       data[k] = js[k]
   return pd.DataFrame(data,index=[js["data_time_stamp"]])


dfs = [read_json(f) for f in snakemake.input]
df = pd.concat(dfs).drop_duplicates(keep="first")
df.to_csv(snakemake.output[0])
