from email.message import EmailMessage
import ssl, smtplib
from flask import Flask
from flask_mail import Mail, Message
import os

app = Flask(__name__)
os.environ['TWILIO_ACCOUNT_SID'] = 'doimspaivbciaqgp'
mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'proyectosprueba26@gmail.com',
    "MAIL_PASSWORD": os.environ['TWILIO_ACCOUNT_SID']
}

app.config.update(mail_settings)
mail = Mail(app)

if __name__ == '__main__':
    
    with app.app_context():
        
        msg = Message(subject="Hello",
                      sender=app.config.get("MAIL_USERNAME"),
                      recipients=["<flrodriguezc22@gmail.com>"], # replace with your email for testing
                      body="This is a test email I sent with Gmail and Python!")
        mail.send(msg)

