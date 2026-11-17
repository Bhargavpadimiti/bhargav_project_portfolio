# Shortcuts for common tasks. Run `make` to see them all.
# Windows without make? Call the script directly: python scripts/portfolio.py <command>

PYTHON ?= python3
CLI    := $(PYTHON) scripts/portfolio.py
TYPE   ?= python

.DEFAULT_GOAL := help
.PHONY: help setup new list test lint update

help: ## Show this help
	@grep -E '^[a-z-]+:.*?## ' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "} {printf "  \033[36m%-8s\033[0m %s\n", $$1, $$2}'

setup: ## One-time setup: git hooks + repo git settings
	$(CLI) setup

new: ## New project: make new NAME=weather-cli [TYPE=python|node|generic] [DESC="..."]
	@test -n "$(NAME)" || (echo "usage: make new NAME=my-project [TYPE=python|node|generic] [DESC=\"...\"]" && exit 1)
	$(CLI) new "$(NAME)" --type "$(TYPE)" $(if $(DESC),--description "$(DESC)")

list: ## List all projects
	$(CLI) list

test: ## Test all projects, or one: make test P=projects/weather-cli
	$(CLI) test $(P)

lint: ## Run every pre-commit check on the whole repo
	pre-commit run --all-files

update: ## Update pre-commit hook versions
	pre-commit autoupdate
