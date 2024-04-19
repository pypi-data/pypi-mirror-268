GLOBALPYTHON := python3.10
CARGO := cargo
GIT := git
PYTHON := venv/bin/python
MATURIN := venv/bin/maturin
PYTEST := venv/bin/pytest
RUSTSOURCES := $(shell find src -name '*.rs')


.PHONY: develop
develop: venv/lib/python3.10/site-packages/pyord/__init__.py

.PHONY: build
build: develop
	$(MATURIN) build


.PHONY: test
test: develop
	$(PYTEST)


venv/lib/python3.10/site-packages/pyord/__init__.py: $(RUSTSOURCES) Cargo.toml Cargo.lock | $(PYTHON)
	$(MATURIN) develop
	@# NOTE: maturin includes the .pyi file in the built module, but to generate it, we need to have the module there
	@# in the first place. So we would need another build after this to build the distribution correctly.
	$(PYTHON) generate_stubs.py pyord pyord.pyi --ruff


$(PYTHON):
	$(GLOBALPYTHON) -m venv venv
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -e '.[dev]'

.PHONY: build-linux-wheels
build-linux-wheels: build-builder-docker-image
	docker run --rm -it -v $(shell pwd):/io $(shell docker build -q -f Dockerfile.build .) build --release

.PHONY: publish-linux-wheels
publish-linux-wheels: build-builder-docker-image
	docker run --rm -it -v $(shell pwd):/io $(shell docker build -q -f Dockerfile.build .) publish

.PHONY: build-builder-docker-image
build-builder-docker-image:
	@# This is redundant, but building this takes such a long time that it's nice to get some output
	@# from the process, which doesn't happen when it's built with the -q flag
	docker build -f Dockerfile.build .
