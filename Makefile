format:
	unimport apps tests
	isort apps tests
	black -l 120 apps tests

test:
	python manage.py test