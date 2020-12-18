import smtplib, ssl
from email.message import EmailMessage

msg = EmailMessage()
msg.set_content("Your_Message")
msg["Subject"] = "Graphics Card"
msg["From"] = "Your_Email"
msg["To"] = ""

context=ssl.create_default_context()

with smtplib.SMTP("smtp.google.com", port=28) as smtp:
    smtp.starttls(context=context)
    smtp.login(msg["From"], "Password_Goes_Here")
    smtp.send_message(msg)

server.quit()
