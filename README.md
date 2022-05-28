# PurpleAir downloader

## Installing
There is a file `readkey_template` that needs to be moved to `.readkey` and the PurpleAir API key should be entered in the template. It will be read by the download program to access the API.

## Running

There are two scripts in the script directory

  1. download_to_json.py -> downloads from the API and saves the native JSON format
  2. write_to_csv.py -> takes a number of JSON files and merges them into a Pandas CSV file

You can run the code from the scripts themselves. e.g. `./scripts/download_to_json.py STATION_ID data.json` and `./scripts/wrf_to_csv.py data1.json data2.json output.csv`. There is also a Makefile that defines two commands `download` and `merge`. 

1. `make download` will define a filename raw_data/YEAR-MONTH-DAY-HOUR-MINUTE.json and check for the file. If it doesn't exist, the download script will run and save to that file (if it does exist, it means you ran the program in the last minute).
2. `make merge` will define a filename data/YEAR-MONTH-DAY.csv and check for the file. If it doesn't exists, the write_to_csv script will run and merge that days json files into a Pandas CSV file (if it does exists, and is not up to date, it should get overwritten).

CL.
