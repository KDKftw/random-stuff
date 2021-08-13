##email function2

import smtplib
import ssl
from email.mime.text import MIMEText

message = """\
Subject:  TTT

Neco je spatne. """


def email():
    ##x= "test message variable"
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "alertserverproblem@gmail.com"
    receiver_email = "ondrej.kadoun@fischer.cz", "ooo.kadoun@gmail.com"
    password = ""
    msg = MIMEText('This is the body of the message.')
    msg['Subject'] = 'Simple test message'

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg)


email()