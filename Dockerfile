# Use a lightweight Python base image
FROM python:3.10-slim

# Copy the uv binary directly from the official Astral image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set the working directory
WORKDIR /app

# Copy the project configuration files created by uv
COPY pyproject.toml uv.lock ./

# Sync the dependencies using uv (creates a virtual environment at /app/.venv)
RUN uv sync --frozen --no-install-project --no-dev

# Add the uv virtual environment to the system PATH
ENV PATH="/app/.venv/bin:$PATH"

# Copy the download script and execute it to bake the model weights into the image
COPY download_model.py .
RUN python download_model.py

# Copy the main API application
COPY app.py .

# Expose the port Snowflake will route traffic to
EXPOSE 8000

# Start the FastAPI server using the environment's uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]