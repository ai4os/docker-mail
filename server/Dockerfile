FROM python:3.8-slim

WORKDIR /app
COPY mail_server.py .
COPY requirements_server.txt /tmp/requirements_server.txt
RUN pip install --no-cache-dir -r /tmp/requirements_server.txt
RUN apt update
RUN apt -y install exim4-daemon-light
EXPOSE 8082
CMD  service exim4 restart & uvicorn mail_server:app --reload --host 0.0.0.0 --port 8082 