.PHONY: docs

docs:
	@python -m pip install Sphinx
	@sphinx-build -b html docs/source/ docs/build/html/
