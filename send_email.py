import smtplib
import os

def send_email(message):
    email = 'damolabalogun79@gmail.com'
    password = os.getenv('PASSWORD')
    host = 'smtp.gmail.com'
    port = 465
    receiver = 'damolabalogun79@gmail.com'

    with smtplib.SMTP_SSL(host, port) as server:
        server.login(email, password)
        server.sendmail(email, receiver, message)

if __name__ == '__main__':
    local_message = f"""\
Subject: News

From: Myself
Hello this is me testing my mail function
"""
    send_email(local_message)