REPOROOT=..
PROTODIRS=$(shell find $(REPOROOT)/arista -name "*.v*" -type d -exec basename {} \;)
DOCTARGETS=$(patsubst %,%.md,$(PROTODIRS))
MODELS_TARGET=models.md

VERSION=$(shell git describe --tags --abbrev=0 || git rev-parse --abbrev-ref HEAD)

.PHONY: default
default: docs

.PHONY: docs
docs: $(DOCTARGETS) $(MODELS_TARGET)
	@echo "Documentation Markdown files generated for Docusaurus."

%.md: FULLNAME = $(basename $@)
%.md: NAME = $(basename $(FULLNAME))
%.md: PROTO = $(REPOROOT)/arista/$(FULLNAME)/$(NAME).proto
%.md: SERVICES = $(REPOROOT)/arista/$(FULLNAME)/services.gen.proto
%.md: DEST = content/models/$(FULLNAME).md
%.md:
	@echo "--- generating "$@" from "$(PROTO)"..."
	@mkdir -p $(dir $(DEST))
	go run generate_markdown.go -root $(REPOROOT) -in $(PROTO) -out $(DEST)

$(MODELS_TARGET):
	@echo "--- generating models index..."
	go run cmd/generate_models_markdown.go -out content/models.md -protodirs "$(PROTODIRS)"

.PHONY: start
start:
	@echo "Starting Docusaurus with version $(VERSION)"
	@VERSION_TAG=$(VERSION) npx docusaurus start

.PHONY: version
version:
	@echo "Creating new Docusaurus versions from tags: $(VERSION)"
	npx docusaurus docs:version $(VERSION)
