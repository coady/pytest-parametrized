check:
	pytest -s --cov

lint:
	ruff .
	ruff format --check .
