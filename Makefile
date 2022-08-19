check:
	pytest -s --cov

lint:
	black --check .
	flake8 --ignore E501
