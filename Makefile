install:
	pip install requirements.txt
	pip install requirements-dev.txt

clean:
	find . -name \*.pyc -delete

lint:
	pylint discover_opendap/discover_opendap.py

test:
	python -m unittest discover tests "*_test.py"
