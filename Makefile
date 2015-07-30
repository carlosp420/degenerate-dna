clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr html/
	rm -rf cover/

coverage: clean-test
	nosetests --verbosity 2 --with-doctest --doctest-extension=rst docs degenerate_dna
	coverage run --source degenerate_dna setup.py test
	coverage report -m
	coverage html

release:
	python setup.py sdist bdist_wheel upload
