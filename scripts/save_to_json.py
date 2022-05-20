import json
from pathlib import Path

try:
    input_filename = snakemake.input[0]
    output_filename = snakemake.output[0]
except NameError:
    import sys
    input_filename = sys.argv[1] # first argument
    output_filename = sys.argv[2] # second argument

output_filename = Path(output_filename)

#make the output directory
output_filename.parent.mkdir(parents=True, exist_ok=True)

#read the file
js = json.load(open(input_filename,'r'))

#save the file
json.dump(js,open(output_filename,'w'))
