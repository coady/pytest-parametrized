check:
	python3 setup.py $@ -mrs
	flake8
	pytest-2.7 --cov 
	pytest --cov --cov-append --cov-fail-under=100

clean:
	hg st -in | xargs rm
	rm -rf build dist pytest_parametrized.egg-info

dist:
	python3 setup.py sdist bdist_wheel
	rst2html.py README.rst $@/README.html
