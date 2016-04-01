.PHONY: test lint unit report-html clean

COVERAGE_OMIT ?= '*/lib*/python*/*,*/pypy-*/*,*/site-packages/*'

test: lint unit
	
lint:
	pep8 *.py

unit:
	coverage erase
	coverage run --append --omit=$(COVERAGE_OMIT) demo_server_test.py
	coverage report --show-missing

# Open the html report in browser
report-html:
	coverage html
	python -m webbrowser -n "file://$(shell pwd)/htmlcov/index.html"

clean:
	rm -rf *.pyc *.log *.log.* .coverage htmlcov/ __pycache__/
