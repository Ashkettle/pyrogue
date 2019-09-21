IMAGE_NAME='Project'
BUILD=1
VERSION=1.0.$(BUILD)

all: clean build test

restore:
	rm -rf .venv
	virtualenv --always-copy .venv
	( \
    . .venv/bin/activate; \
    pip install -r requirements.txt; \
    )

	
	

python-test: 
	( \
    . .venv/bin/activate; \
    python3 -m pytest --cov-report term --cov-report html:cov_html --cov-report xml:cov.xml --cov=game test/; \
    )
	

lint: python-build

python-build:
	( \
    . .venv/bin/activate; \
    pylint -j 4 game; \
    )
	


build: python-build python-test

test: python-test

run:
	( \
    . .venv/bin/activate; \
    python3 game/main.py; \
    )
	

clean:
	find . -type f -name "*.pyc" -delete
	rm -rf $(find . -type d -name .pytest_cache)
