check:
	python3 setup.py $@ -ms
	black --$@ -q .
	flake8
	pytest --cov --cov-fail-under=100
