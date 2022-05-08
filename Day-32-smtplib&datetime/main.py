# sending emails using Python
import smtplib

# working with datetime module
import datetime as dt
import random

my_email = "basemelshafei1997@gmail.com"
password = 'password'

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 3:
    with open('quotes.txt') as file:
        list_of_quotes = file.readlines()
        quote = random.choice(list_of_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs='elshafeibasem@yahoo.com',
                            msg=f"Subject: Email from Python. Today's quote \n{quote}")
















