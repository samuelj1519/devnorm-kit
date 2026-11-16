.PHONY: verify test check
PYTHON ?= python3

verify:
	$(PYTHON) -B scripts/package.py verify

test:
	PYTHONDONTWRITEBYTECODE=1 $(PYTHON) -m unittest discover -s tests -v

check: verify test
	git diff --check
