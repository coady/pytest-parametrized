check:
	pytest --cov

lint:
	black --check .
	flake8
