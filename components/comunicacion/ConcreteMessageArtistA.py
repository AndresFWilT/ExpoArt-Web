from email.message import Message
from msilib.schema import Error
from flask_mail import Mail, Message
import os

class ConcreteMessageArtistA(Message):
     # global
    __data = {}

    def __init__(self, data) -> None:
        """
        constructor
        """
        self.data = data.to_dict()


    def operation_implementation(self,app) -> str:
        try:
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
            msg = Message( self.data['subject'],
                        sender=app.config.get("MAIL_USERNAME"),
                        recipients=[self.data['receiver']], # replace with your email for testing
                        body= self.data['message'])
            print(msg)
            mail.send(msg)


            return "Correo enviado"
        except Exception as e:
            print(e)
            return "No se pudo enviar el correo"



    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data


