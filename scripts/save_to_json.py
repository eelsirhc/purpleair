import json

js = json.load(open(snakemake.input[0],'r'))
json.dump(js,open(snakemake.output[0],'w'))
