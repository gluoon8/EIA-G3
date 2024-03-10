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
	 find src -name "*.F90" -exec fprettify {} \;
	
.PHONY: docs
docs:
	doxygen
