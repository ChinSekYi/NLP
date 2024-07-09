install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
	python -m textblob.download_corpora

test:
	#python -m pytest -vv --cov=hello --cov=hellocli test_*.py

format:
	isort *.py
	black *.py

lint:
	pylint --disable=R,C  *.py

all: install format lint test