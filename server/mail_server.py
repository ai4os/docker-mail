from fastapi import FastAPI
import os
import subprocess

token_env_name = "MAILING_TOKEN"
token_val = os.getenv(token_env_name)

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'server is UP'}

@app.get("/notify")
def notify(email: str, body: str, subject: str, token: str):

    if token == token_val:
        send_mail(email, body, subject)
        return {"status": "ok", "message": "Notification sent successfully"}
    else:
        return {"status": "error", "message": "Invalid token, notification not sent"}
    


def send_mail(email: str, body: str, subject: str):
  
    print(email, body, subject);

    bash_command = f"echo '{body}' | mail -s '{subject}' {email}"

    try:
        subprocess.run(bash_command, check=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    except subprocess.CalledProcessError as e:
        print(e.stderr)

