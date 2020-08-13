import smtplib, os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
load_dotenv()

email = os.getenv('GMAIL_EMAIL')
password = os.getenv('GMAIL_PASSWORD')


def sendEmail(previousEquityClose, currentEquity):
    sentFrom = 'Luis Raspberry Pi'
    to = 'luissoccerstar@gmail.com'
    if previousEquityClose == currentEquity:
        subject = 'Sorry better luck tomorrow'
    elif currentEquity > previousEquityClose:
        subject = 'Good Job on the Trading Today!'
    elif currentEquity < previousEquityClose:
        subject = 'Today was a rough day maybe tomorrow'
    else:
        subject = 'Whoops something went wrong'

    msg = MIMEMultipart()
    msg['From'] = sentFrom
    msg['To'] = to
    msg['Subject'] = subject
    text = msg.as_string()

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(email, password)
    server.sendmail(sentFrom, to, text)
    server.close()

    print('Mail Sent')
