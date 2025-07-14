format:
	unimport apps tests
	isort apps tests
	black -l 120 apps tests

test:
	coverage run manage.py test
	coverage report --fail-under=90