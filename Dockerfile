FROM python:3.12-slim-bookworm

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml uv.lock* ./

RUN uv venv && uv pip install --upgrade pip && uv sync --locked

COPY . .

CMD ["uv", "run", "run.py"]