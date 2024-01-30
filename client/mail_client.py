import os
import requests


from dateutil import parser


def send_mail(email: str, body: str, subject: str, token: str):
    api_url = "http://192.168.1.3:8082/notify"
    params = {"email": email, "body": body, "subject": subject, "token": token}

    response = requests.get(api_url, params)
    data = response.json()
    print(data)


def get_current_date():
    global current_date
    url = "http://worldtimeapi.org/api/timezone/Europe/Madrid"
    response = requests.get(url)
    data = response.json()
    current_date = parser.parse(data["datetime"])

    return current_date


def compare_date(date):
    current_date = get_current_date()
    diff = current_date - date

    return diff.days > int(os.getenv("NUM_DAYS", 7))


def main():
    date = parser.parse(os.getenv("DATE").strip('"'))
    mail = os.getenv("DEST")
    body = os.getenv("BODY").strip('"')
    subject = os.getenv("SUBJECT").strip('"')
    token = os.getenv("MAILING_TOKEN")

    if compare_date(date):
        send_mail(mail, body, subject, token)


main()
