FROM python:3.11-slim

WORKDIR /app

RUN pip install fastapi requests uvicorn

COPY . .

WORKDIR /app/code
CMD ["python3", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

