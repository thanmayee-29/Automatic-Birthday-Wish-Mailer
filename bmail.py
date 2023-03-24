import pandas as pd
from email.message import EmailMessage
from email.mime.text import MIMEText #only text based-content
import smtplib
from datetime import datetime


df = pd.read_excel('your_bdays_list.xlsx')
today = datetime.now().date()
today_bdays = df[df['birthday'].dt.date == today]

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('enter your email', 'Authorized-app-password')
#the Authorized-app-password can be generated in the gmail-account-manage-->security-->enable 2step verification-->App passwords-->select app and device-->generate

for index, row in today_bdays.iterrows():
    name = row['name']
    email = row['email']
    message = f'{name} your birthday message'
    msg = MIMEText(message)
    msg['Subject'] = 'Look who\'s shining all in their glory!'
    msg['From'] = 'enter your email'
    msg['To'] = email
    server.sendmail('enter your email', email, msg.as_string())

server.quit()
