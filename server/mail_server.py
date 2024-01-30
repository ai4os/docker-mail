import os
import subprocess

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi


token_env_name = "MAILING_TOKEN"
token_val = os.getenv(token_env_name)

app = FastAPI()


@app.get("/")
async def status():
    return {"message": "server is UP"}


@app.get("/notify")
def notify(email: str, body: str, subject: str, token: str):
    if token == token_val:
        send_mail(email, body, subject)
        return {"status": "ok", "message": "Notification sent successfully"}
    else:
        return {"status": "error", "message": "Invalid token, notification not sent"}


def send_mail(email: str, body: str, subject: str):
    print(email, body, subject)

    bash_command = f"echo '{body}' | mail -s '{subject}' {email}"

    try:
        subprocess.run(
            bash_command,
            check=True,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
    except subprocess.CalledProcessError as e:
        print(e.stderr)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="Mail-Service",
        version="1.0.0",
        description="Service for sending mails",
        routes=app.routes,
    )

    app.openapi_schema = openapi_schema

    return app.openapi_schema


app.openapi = custom_openapi
