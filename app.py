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
    cnt +=('<b>Top Stories:</>\n' + '<br> ')
