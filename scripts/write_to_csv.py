import pandas as pd
import json
from pathlib import Path

def read_json(filename):
   js = json.load(open(filename,'r'))
   data = dict()
   data.update(dict(zip(js["fields"],js["data"][0])))
   for k in ["api_version", "time_stamp", "data_time_stamp"]:
       data[k] = js[k]
   return pd.DataFrame(data,index=[js["data_time_stamp"]])

def process_json_files(input_files, output):
   dfs = [read_json(f) for f in input_files]
   df = pd.concat(dfs).drop_duplicates(keep="first")
   output.parent.mkdir(exist_ok=True, parents=True)
   df.to_csv(output)


if __name__ == "__main__":
   try:
        input_files = snakemake.input
        output_filename = snakemake.output[0]
   except NameError:
        import sys
        input_files = sys.argv[1:-1]
        output_filename = sys.argv[-1]
        output_filename = Path(output_filename)
   process_json_files(input_files, output_filename)
