REPOROOT=../
PROTODIRS=$(shell find $(REPOROOT)/arista -name "*.v*" -type d -exec basename {} \;)
DOCTARGETS=$(patsubst %,%.md,$(PROTODIRS))

.PHONY: default
default: docs

.PHONY: docs
docs: $(DOCTARGETS)
	hugo --gc --minify --cleanDestinationDir

%.md: FULLNAME = $(basename $@)
%.md: NAME = $(basename $(FULLNAME))
%.md: PROTO = $(REPOROOT)/arista/$(FULLNAME)/$(NAME).proto
%.md: SERVICES = $(REPOROOT)/arista/$(FULLNAME)/services.gen.proto
%.md: DEST = content/models/$(FULLNAME).md
%.md:
	@echo "--- generating "$@" from "$(PROTO)"..."
	protoc -I $(REPOROOT) \
		--doc_out=content/models --doc_opt=./model.tmpl,$(FULLNAME).body \
		$(PROTO) $(SERVICES)
	echo "---\ntitle: $(FULLNAME)\n---\n\n" > $(DEST)
	cat content/models/$(FULLNAME).body >> $(DEST)
	rm content/models/$(FULLNAME).body
