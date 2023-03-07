
install-dependencies:
	poetry install

run-hello-world:
	poetry run python poetry_demo/Demo.py

run-hello-world-script:
	poetry run demo

run-test:
	poetry run pytest
