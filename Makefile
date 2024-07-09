install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
	python -m textblob.download_corpora

test:
	python -m pytest -vv --cov=wiki_phrases --cov=nlplogic test_*.py

format:
	isort *.py nlplogic
	black *.py

lint:
	pylint --disable=R,C  *.py nlplogic/*.py

all: install format lint test