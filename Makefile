date := $(shell date +%Y-%m-%d)
time := $(shell date +%Y-%m-%d-%H-%M)

station_id = 96227\
	     138000


merge_suffix=_$(date).csv
download_suffix=_$(time).json

download_targets = $(patsubst %.end,%

merge_targets=$(addprefix data/, $(addsuffix $(merge_suffix), $(station_id)))
download_targets=$(addprefix raw_data/, $(addsuffix $(download_suffix), $(station_id)))

splits=$(word $2, $(subst _, ,$1))
dots=$(word $2, $(subst ., ,$1))

download: $(download_targets)
merge : $(merge_targets)


data/%: $(shell find raw_data -name '$**')
	python scripts/write_to_csv.py raw_data/$(call dots,$*,1)* $@

raw_data/% :
	python scripts/download_to_json.py $(call splits,$*,1) $@

