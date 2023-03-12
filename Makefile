check:
	pytest -s --cov

lint:
	black --check .
	ruff .
