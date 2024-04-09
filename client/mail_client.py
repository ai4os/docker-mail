import os
import requests
import datetime

def send_mail(email: str, body: str, subject: str, token: str):
    api_url = "https://api.cloud.ai4eosc.eu:5000/notify"
    params = {"email": email, "body": body, "subject": subject, "token": token}

    response = requests.get(api_url, params)
    data = response.json()
    print(data)


def compare_date(date):
    
    date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
    current_date = datetime.date.today()
    
    diff = current_date - date

    print(diff.days)
    return diff.days > int(os.getenv("NUM_DAYS", 7).strip('"'))


def main():
    try:
        date = os.getenv("DATE").strip('"')
        mail = os.getenv("DEST").strip('"')
        body = os.getenv("BODY").strip('"')
        subject = os.getenv("SUBJECT").strip('"')
        token = os.getenv("MAILING_TOKEN").strip('"')

        if compare_date(date):
            send_mail(mail, body, subject, token)

    except Exception as e:
        print(f"Error: {e}")


main()
