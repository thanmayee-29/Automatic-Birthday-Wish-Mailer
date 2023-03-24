import pandas as pd
from email.message import EmailMessage
from email.mime.text import MIMEText
import smtplib
from datetime import datetime
import emoji

'''filename = 'your_bdays_list.xlsx'
if os.access(filename, os.R_OK):
    print(f"File {filename} is readable")
else:
    print(f"File {filename} is not readable")
'''

df = pd.read_excel('your_bdays_list.xlsx')
today = datetime.now().date()
today_bdays = df[df['birthday'].dt.date == today]

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('janapareddythanmayee29@gmail.com', 'ygqyjjuntjqlbjkt')

for index, row in today_bdays.iterrows():
    name = row['name']
    email = row = row['email']
    message = f'{name} Thanu hopes that we can always be together on this life-adventure. You know Thanu will always be your best of friends right!!? and so HAPPY BIRTHDAY {name}!! may all your wishes be gold.'
    msg = MIMEText(message)
    msg['Subject'] = 'Look who\'s shining all in their glory!'
    msg['From'] = 'janapareddythanmayee29@gmail.com'
    msg['To'] = email
    server.sendmail('janapareddythanmayee29@gmail.com', email, msg.as_string())

server.quit()
