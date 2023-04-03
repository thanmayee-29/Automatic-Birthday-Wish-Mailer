import pandas as pd
# from email.message import EmailMessage
from email.mime.text import MIMEText
# from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import smtplib
from datetime import datetime
# from email import encoders
from urllib.request import urlopen


df = pd.read_excel('your_bdays_list.xlsx')
today = datetime.now().date()
today_bdays = df[df['birthday'].dt.date == today]
msg = MIMEMultipart()
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('janapareddythanmayee29@gmail.com', 'ygqyjjuntjqlbjkt')

for index, row in today_bdays.iterrows():
    name = row['name']
    email = row['email']

    text = f'{name} Thanu hopes that we can always be together on this life-adventure. You know that Thanu will always be your best of friends right!!? and so HAPPY BIRTHDAY {name}!! May all your wishes come true.'
    part1 = MIMEText(text, "plain")
    msg.attach(part1)

    url = "file:///C:/Users/yowaisquad/OneDrive/Documents/cake/wishes.html"
    html_content = urlopen(url).read().decode('utf-8')
    body = MIMEText(html_content, 'html')
    msg.attach(body)

msg['Subject'] = 'Look who\'s shining on their glorious day!!'
msg['From'] = 'janapareddythanmayee29@gmail.com'
msg['To'] = email
server.sendmail('janapareddythanmayee29@gmail.com', email, msg.as_string())


server.quit()
