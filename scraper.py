import requests
from bs4 import BeautifulSoup
import smtplib
import time

# -*- coding: utf-8 -*-

url = 'https://www.amazon.in/Selpak-3Ply-Toilet-Tissue-Paper/dp/B01N2Z3RMU/ref=sr_1_2?dchild=1&keywords=toilet+paper&qid=1587901510&s=hpc&sr=1-2'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'}

def check_price():
	page = requests.get(url, headers=headers)

	soup = BeautifulSoup(page.text, "html.parser")

	title = soup.find(id="productTitle").get_text()
	price = soup.find(id="priceblock_ourprice").get_text()
	converted_price = float(price[1:3])

	if (converted_price < 500):
		send_mail()

	print(converted_price)
	print(title.strip())

	if(converted_price < 500):
		send_mail()

def send_mail():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login('yash.patki1@gmail.com','pczbcghjmgwtfklt')

	# subject = 'Hey, the price is down!'
	# body = 'Check the link https://www.amazon.in/Selpak-3Ply-Toilet-Tissue-Paper/dp/B01N2Z3RMU/ref=sr_1_2?dchild=1&keywords=toilet+paper&qid=1587901510&s=hpc&sr=1-2'

	msg = """\

	Subject: Price is down!
			 check link = https://www.amazon.in/Selpak-3Ply-Toilet-Tissue-Paper/dp/B01N2Z3RMU/ref=sr_1_2?dchild=1&keywords=toilet+paper&qid=1587901510&s=hpc&sr=1-2"""

	server.sendmail(
			'yash.patki1@gmail.com',
			'yash.patki6@gmail.com',
			msg)
	print("Email sent!")

	server.quit()

while True:
	check_price()
	time.sleep(60*60*24*7)