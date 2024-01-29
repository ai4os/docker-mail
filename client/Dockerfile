FROM python:3.8-slim

WORKDIR /app

RUN pip install requests python-dateutil

COPY mail_client.py .
CMD ["python", "./mail_client.py"]

