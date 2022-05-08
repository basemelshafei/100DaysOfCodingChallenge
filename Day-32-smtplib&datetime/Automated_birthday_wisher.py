import datetime as dt
import smtplib
import pandas as pd
import random

my_email = "basemelshafei1997@gmail.com"
password = 'password'

now = dt.datetime.now()
today_month = now.month
today_day = now.day
today = (today_month, today_day)

birthdays = pd.read_csv('birthdays.csv')

birthdays_dict = {(birthdays_row['month'], birthdays_row['day']): birthdays_row for (index, birthdays_row) in birthdays.iterrows()}

if (today_month, today_day) in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f'letter_templates/letter_{random.randint(1, 3)}.txt'
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person['name'])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person['email'],
                            msg=f"Subject: Happy Birthday!\n\n {contents}")

























