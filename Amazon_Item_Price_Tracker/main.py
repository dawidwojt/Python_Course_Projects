#This app checkes for the price of your item and when it is below your max price it sends an email to your account.
import requests
from bs4 import BeautifulSoup
import smtplib
url = "https://www.amazon.com/Samsung-Qualcomm-Snapdragon-Included-Productivity/dp/B09NQM7XHC/ref=sr_1_1_sspa?"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
    "Accept-Language": "en-GB,en;q=0.9,pl-PL;q=0.8,pl;q=0.7,en-US;q=0.6"
}
my_email = "youeemail@gmail.com"
password = "your_password"

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")

the_current_price = soup.find(name="span", class_="a-offscreen").getText()
the_current_price = float(the_current_price[1:])
max_price = 750

if the_current_price < max_price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="your_email@outlook.com",
                            msg=f"Subject: PRODUCT PRICE ALERT \n\n The product's price we keep track on is now below your ${max_price} \n\n Now the current price is: {the_current_price} \n\n Check it out: {url}")