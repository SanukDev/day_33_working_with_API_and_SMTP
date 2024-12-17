import requests
from datetime import datetime
import smtplib
import time

MY_LAT = -15.774898
MY_LONG = -47.880569

parameters = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'formatted': 0,
}


def is_iss():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()

    latitude_iss = float(data['iss_position']['latitude'])
    longitude_iss = float(data['iss_position']['longitude'])

    if MY_LAT-5 <= latitude_iss <= MY_LAT+5 and MY_LONG-5 <= longitude_iss <= MY_LONG+5:
        return True


def is_night():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    data = response.json()

    sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])
    sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])

    now = datetime.now().hour
    if now >= sunset or now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()

            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr="samukakaroto123@gmail.com", to_addrs="samukakaroto123@gmail.com",
                                msg="Subject:Hello!! look Up now!\n\n The ISS is above you now in the sky!"
                                )