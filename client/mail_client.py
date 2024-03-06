import os
import requests


from dateutil import parser


def send_mail(email: str, body: str, subject: str, token: str):
    api_url = "https://api.cloud.ai4eosc.eu:5000/notify"
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

    return diff.days > int(os.getenv("NUM_DAYS", 7).strip('"'))


def main():
    try:
        date = parser.parse(os.getenv("DATE").strip('"'))
        mail = os.getenv("DEST").strip('"')
        body = os.getenv("BODY").strip('"')
        subject = os.getenv("SUBJECT").strip('"')
        token = os.getenv("MAILING_TOKEN").strip('"')

        if compare_date(date):
            send_mail(mail, body, subject, token)

    except Exception as e:
        print(f"Error: {e}")


main()
