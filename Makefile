.PHONY: formatpy
format-py:
	isort .
	black .

.PHONY: formatsh
format-sh:
	shellcheck .
	shfmt .

.PHONY: formatf90
format-f90:
	fprettify src/*
	
.PHONY: docs
docs:
	doxygen
