FROM python:3.9-slim

WORKDIR /app

COPY ./server /app/server
COPY ./requirements.txt /app

RUN pip install --no-cache-dir -r /app/requirements.txt

CMD ["uvicorn", "server.main:app", "--host", "0.0.0.0", "--port", "8000"]
