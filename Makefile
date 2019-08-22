check:
	python3 setup.py $@ -ms
	black --$@ -q .
	flake8
	pytest-2.7
	pytest --cov --cov-fail-under=100
