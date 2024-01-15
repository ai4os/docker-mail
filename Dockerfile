FROM python:3.8-slim

WORKDIR /app

RUN pip install requests python-dateutil

COPY mail.py .
CMD ["python", "./mail.py"]

