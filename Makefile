date := $(shell date +%Y-%m-%d)
time := $(shell date +%Y-%m-%d-%H-%M)

merge_target=data/$(date).csv
download_target=raw_data/$(time).json

today=$(wildcard raw_data/$(date)*.json)

download: $(download_target)
merge : $(merge_target)


$(merge_target) :  $(today)
	python scripts/write_to_csv.py $(today) $@

${download_target} : 
	python scripts/download_to_json.py $@
