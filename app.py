# HTTP requests
import requests

#Web scraping
from bs4 import BeautifulSoup

#send email
import smtplib

#email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#date and time manipulation
import datetime
now=datetime.datetime.now()

#email content placeholder
content = ''

#Extracting News From Source
#I'm using Hacker News

def extract_news(url):
    print('Extracting News Stories')
    cnt = ''
    cnt +=('<b>Top Stories:</>\n' + '<br>' + '-' * 50 + '<br>')
    response = request.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    for i, tag in enumerate(soup.find_all('td', attrs={'class':'title', 'valign' : ''})):
        cnt += ((str(i + 1) + ' :: ' + '+tag.text + "/n" + '<br>' ) if tag.text!= 'More' else '')
    return(cnt)

cnt = extract_news('https://news.ycombinator.com/')
content += cnt
content += ('<br>-------<br>')
content += ('<br><br>End of Message')


#email sending
print('Composing email')

# plugin your email information
SERVER = 'smtp.gmail'
PORT = 587
FROM = '' #email id
TO = '' #your to email id can be a list
PASS = ' '#email password


msg = MIMEMultipart()
