FROM python:3.11-slim

# Install dependencies for building/installing poetry & your app
RUN apt-get update && apt-get install -y curl build-essential && rm -rf /var/lib/apt/lists/*

# Install Poetry (latest official way)
RUN curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to PATH environment variable
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

# Copy only dependency files first for caching
COPY pyproject.toml poetry.lock* /app/

# Install dependencies without creating a virtual env
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --only main

# Copy rest of app code
COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
