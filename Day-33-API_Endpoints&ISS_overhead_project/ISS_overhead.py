import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude
my_position = (MY_LONG, MY_LAT)
my_email = 'basemelshafei@gmail.com'
my_password = "Password"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
iss_position = (iss_longitude, iss_latitude)

#Your position is within +5 or -5 degrees of the ISS position.

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
hour_now = time_now.hour
print(hour_now)

#If the ISS is close to my current position

def can_see():
    if -5 < my_position[0] - iss_position[0] < 5 and -5 < my_position[1] - iss_position[1] < 5:
        return True
    else:
        return False

print(can_see())

# and it is currently dark

def is_night():
    if sunrise > hour_now > sunset :
        return True
    else:
        return False

print(is_night())


# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

while True:
    time.sleep(60)
    if can_see() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=my_email,
                                msg=f"Subject: Look Up!\n\n ISS is currently over your head.")






