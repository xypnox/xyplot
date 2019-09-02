freeze:
	pip freeze | grep -v "pkg-resources" > requirements.txt

build: /* setup.py
	rm -fr build/* dist/*
	python3 setup.py sdist bdist_wheel

docs: README.md xyplot/*
	pdoc3 --html xyplot --output-dir docs

publish: build
	twine upload dist/*