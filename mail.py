import smtplib
from email.message import EmailMessage

import os
import requests
from dateutil import parser

def send_mail():
    msg = EmailMessage()
    
    #Mail content
    msg.set_content("The execution of the job has begun at : " + str(current_date))

    msg['Subject'] = 'DOCKER TEST'
    msg['From'] = "testcorreodocker@gmail.com"
    msg['To'] = os.getenv("DEST")

    # SMP Server Config
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    server.login("testcorreodocker@gmail.com", os.getenv("PSWD").strip('"'))
    server.send_message(msg)
    server.quit()

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
    if compare_date(date):
        send_mail()

main()