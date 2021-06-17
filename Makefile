check:
	pytest -s --cov

lint:
	black --check .
	flake8
