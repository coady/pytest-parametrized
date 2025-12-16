check:
	uv run pytest -s --cov

lint:
	uvx ruff check
	uvx ruff format --check
