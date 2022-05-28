date := $(shell date +%Y-%m-%d)
time := $(shell date +%Y-%m-%d-%H-%M)

prefix=.
data=$(prefix)/data/
raw_data=$(prefix)/raw_data/

station_id = 96227\
	     138000


merge_suffix=_$(date).csv
download_suffix=_$(time).json

download_targets = $(patsubst %.end,%

merge_targets=$(addprefix $(data), $(addsuffix $(merge_suffix), $(station_id)))
download_targets=$(addprefix $(raw_data), $(addsuffix $(download_suffix), $(station_id)))

splits=$(word $2, $(subst _, ,$1))
dots=$(word $2, $(subst ., ,$1))


download: $(raw_data) $(download_targets)
merge : $(data) $(merge_targets)

$(raw_data):
	mkdir $(raw_data)

$(data):
	mkdir $(data)

%.csv: $(shell find $(raw_data) -name '$(*F)*')
	@ python scripts/write_to_csv.py $(shell find $(raw_data) -name '$(*F)*') $@

%.json:
	python scripts/download_to_json.py $(call splits,$(@F),1) $@

