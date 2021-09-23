# Run this to run unit tests and format the code
format:
	black ./
test:
	flake8 \
		--max-line-length 88 \
		--extend-ignore E203
