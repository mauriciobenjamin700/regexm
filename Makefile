lint-fix:
	uv run black validators
	uv run isort validators
	uv run ruff check validators --fix