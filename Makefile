.PHONY: help install sync format lint type-check clean example

help:
	@echo "Available commands:"
	@echo "  make install      - Install package in development mode"
	@echo "  make sync         - Sync all dependencies (including dev)"
	@echo "  make format       - Format code with ruff"
	@echo "  make lint         - Lint code with ruff"
	@echo "  make type-check   - Type check with pyright"
	@echo "  make example      - Run example generation"
	@echo "  make clean        - Clean build artifacts and cache"
	@echo "  make all          - Format, lint, and type-check"

install:
	uv pip install -e .

sync:
	uv sync --extra dev

format:
	ruff format src/ examples/
	ruff check --fix src/ examples/

lint:
	ruff check src/ examples/

type-check:
	pyright src/ examples/

example:
	cd examples/simple-sensor-network && ./generate.sh

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .ruff_cache
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

all: format lint type-check
