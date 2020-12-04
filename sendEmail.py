import smtplib, ssl
from email.message import EmailMessage

msg = EmailMessage()
msg.set_content("It worked")
msg["Subject"] = "Graphics Card"
msg["From"] = "esamkriegel@gmail.com"
msg["To"] = "elyskrie21@pellaschools.org"

context=ssl.create_default_context()

with smtplib.SMTP("smtp.google.com", port=28) as smtp:
    smtp.starttls(context=context)
    smtp.login(msg["From"], "ill77mon")
    smtp.send_message(msg)

server.quit()
