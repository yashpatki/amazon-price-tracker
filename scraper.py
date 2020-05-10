import requests
from bs4 import BeautifulSoup
import smtplib
import time
import PySimpleGUI as sg

# -*- coding: utf-8 -*-

# gui code
sg.theme("DarkAmber")
# Stuff inside the window
layout = [
    [sg.Text("Amazon Price Tracker")],
    [sg.Text("Enter url for product"), sg.InputText()],
    [sg.Text("Enter the max price"), sg.InputText()],
    [sg.Text("Enter your email"), sg.InputText()],
    [sg.Button("Ok"), sg.Button("Cancel")],
]

# Create the Window
window = sg.Window("Window Title", layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, "Cancel"):  # if user closes window or clicks cancel
        break
    url, maxprice, r_email = values[0], values[1], values[2]

window.close()

# scraper code
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36"
}


def check_price():
    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.text, "html.parser")

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:3])

    if converted_price <= maxprice:
        send_mail()

    # print(converted_price)


# print(title.strip())


def send_mail():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("yash.patki1@gmail.com", "pczbcghjmgwtfklt")

    server.sendmail("yash.patki1@gmail.com", r_email, "Price is down. Check :" + url)
    print("Email sent!")

    server.quit()


while True:
    check_price()
# time.sleep(60*60*24*7)
