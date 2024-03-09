check:
	pytest -s --cov

lint:
	ruff check .
	ruff format --check .
