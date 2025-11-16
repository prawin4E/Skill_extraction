.PHONY: help install install-dev test lint format clean run docker-build docker-run docker-stop

help:  ## Show this help message
	@echo "Usage: make [target]"
	@echo ""
	@echo "Available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-20s %s\n", $$1, $$2}'

install:  ## Install production dependencies
	pip install -r requirements.txt
	python -m spacy download en_core_web_lg
	python setup.py install

install-dev:  ## Install development dependencies
	pip install -r requirements.txt
	python -m spacy download en_core_web_lg
	pre-commit install

test:  ## Run tests with coverage
	pytest tests/ -v --cov --cov-report=term-missing --cov-report=html

test-quick:  ## Run tests without coverage
	pytest tests/ -v

lint:  ## Run all linting checks
	@echo "Running Black..."
	black --check .
	@echo "Running isort..."
	isort --check-only .
	@echo "Running flake8..."
	flake8 .
	@echo "Running mypy..."
	mypy . --ignore-missing-imports || true
	@echo "Running bandit..."
	bandit -r . -ll --skip B101 || true

format:  ## Format code with black and isort
	black .
	isort .

clean:  ## Clean up generated files
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf build/ dist/ .pytest_cache/ .coverage htmlcov/ coverage.xml

run:  ## Run the development server
	uvicorn main:app --reload --host 0.0.0.0 --port 8000

run-prod:  ## Run the production server
	uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4

docker-build:  ## Build Docker image
	docker-compose build

docker-run:  ## Run Docker container
	docker-compose up

docker-stop:  ## Stop Docker container
	docker-compose down

docker-clean:  ## Remove Docker image and containers
	docker-compose down -v --rmi all

pre-commit-install:  ## Install pre-commit hooks
	pre-commit install

pre-commit-run:  ## Run pre-commit on all files
	pre-commit run --all-files
