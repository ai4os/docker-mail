import os
import requests
from dateutil import parser

def send_mail(email: str, body: str, subject: str, token: str):
    
    api_url = "http://127.0.0.1:8000/notify"
    params = {"email": email, "body": body, "subject": subject, "token": token}

    try:
    
        response = requests.get(api_url, params)
        response.raise_for_status()

        data = response.json()
        return data
    
    except requests.exceptions.RequestException as e:
        return {"status": "error", "message": f"Error en la solicitud a la API: {str(e)}"}

def get_current_date():

    global current_date
    url = "http://worldtimeapi.org/api/timezone/Europe/Madrid"
    response = requests.get(url)
    data = response.json()
    current_date = parser.parse(data['datetime'])
    
    return current_date

def compare_date(date):

    current_date = get_current_date()
    diff = current_date - date
    
    return diff.days > int(os.getenv("NUM_DAYS", 7))

def main():

    date = parser.parse(os.getenv("DATE").strip('"'))
    mail = parser.parse(os.getenv("DEST").strip('"'))
    body = parser.parse(os.getenv("BODY").strip('"'))
    subject = parser.parse(os.getenv("SUBJECT").strip('"'))

    if compare_date(date):
        send_mail(mail, body, subject)

main()