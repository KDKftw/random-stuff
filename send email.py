##email function

import smtplib, ssl


## enable outside apps https://www.google.com/settings/security/lesssecureapps


def email(message):
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "alertserverproblem@gmail.com"
    receiver_email = "ondrej.kadoun@fischer.cz", "ooo.kadoun@gmail.com"
    password = ""





    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)



email("testhesd")