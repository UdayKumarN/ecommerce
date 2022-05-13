from importlib import reload
import time
from email.header import Header
from email.message import EmailMessage
import smtplib
import configparser
config=configparser.RawConfigParser()
config.read(".\\configuration\\email.ini")

class configur:
    @staticmethod # to Static method used to call directly without creating object
    def gerusername():
        username=config.get('credentials','sender_email')
        return username

    @staticmethod
    def getpassword():
        password=config.get('credentials','password')
        return password

class emailutil(configur):

    def __init__(self):
        print("preparing for email")

    def send_email(self):
        email_list = {
            'udaykumarnarsingoju@gmail.com',
            'vk798964@gmail.com',
        }
        sender_name = "Uday"
        subject = f'Test execution report & attachment'
        content = f"Hi,\n" \
                  f"Execution of test suite is finished\n" \
                  f"Logs and reports attached.\n\n" \
                  f"Regards\n" \
                  f"{sender_name}"

        with open(r"C:\Users\udayk\PycharmProjects\ecommerce\report.html","r") as f:
            f.close()
            time.sleep(2)
            #reload()
        with open("report.html", "rb+") as file:
            data = file.read()
            #print("data in binary :", data)
            fname = file.name
            print("file name:", fname)
        user=configur.gerusername()
        pw=configur.getpassword()
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
         # Make sure to give app access in your Google account
        server.login(user, pw)
        email = EmailMessage()
        email['From'] = user
        email['To'] = email_list
        email['Subject'] = subject
        email.set_content(content)
        email.add_attachment(data,maintype='application',subtype="html",filename=fname)

        server.send_message(email)
        print("Email sent!!")

#send_email()
