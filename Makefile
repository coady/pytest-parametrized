check:
	uv run pytest -s --cov

lint:
	uv run ruff check
	uv run ruff format --check
