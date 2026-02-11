FROM python:3.12

WORKDIR /app

# Install runtime deps
RUN pip install --no-cache-dir fastapi uvicorn requests jinja2

# Copy app code
COPY src /app/src

EXPOSE 8000

# Start FastAPI (THIS is what keeps container alive)
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
