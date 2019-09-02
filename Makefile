freeze:
	pip freeze | grep -v "pkg-resources" > requirements.txt

build: freeze /* setup.py
	rm -fr build/* dist/*
	python3 setup.py sdist bdist_wheel

docs: README.md xyplot/*
	rm -rf docs
	pdoc3 --html xyplot --output-dir docs

publish: build
	twine upload dist/* --verbose
