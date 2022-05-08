import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

url = "https://www.amazon.co.uk/Ace-Data-Science-Interview-Questions/dp/0578973839/ref=sr_1_1?keywords=ace+the+data+science+interview&qid=1650301337&sprefix=ace+the+data%2Caps%2C73&sr=8-1"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15",
    "Accept-Language": "en-GB,en;q=0.9"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())


for ID in soup.find_all('div', id=True):
    print(ID.get('id'))


price = soup.find(id="corePrice_feature_div").get_text()
price_without_currency = price.split("£")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 200

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )













