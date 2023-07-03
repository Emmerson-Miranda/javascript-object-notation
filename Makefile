.PHONY: test lint tox coverage dist

venv/bin/activate: requirements.txt
	python3 -m venv venv
	./venv/bin/pip3 install -r requirements.txt

test: venv/bin/activate
	pytest --cache-clear -v ./tests

clear:
	rm -rf __pycache__
	rm -rf venv
	rm -rf dist
	rm -rf build
	rm -rf *.egg-info
	rm -rf .eggs
	rm -rf .pytest_cache

run: test
	#source venv/bin/activate
	./venv/bin/pip3 wheel --no-deps -w dist .
	twine check dist/*
	#(venv) $ twine upload -r testpypi dist/*
    #(venv) $ twine upload dist/*

