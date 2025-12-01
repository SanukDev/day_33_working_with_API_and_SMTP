ISS Overhead Notifier


This Python script checks whether the International Space Station (ISS) is currently above your location during nighttime.
If both conditions are true, the script automatically sends you an email alert so you can look up and try to spot the ISS in the sky.


How It Works


The script runs in an infinite loop, checking every 60 seconds:
is_iss()
Currently returns True by default — this function should be expanded to check the real-time ISS position using an API such as:
http://api.open-notify.org/iss-now.json
is_night()
Uses the Sunrise-Sunset API to determine if it is currently nighttime at your location.
API: https://api.sunrise-sunset.org/json
Extracts sunrise and sunset times
Compares them with the current local hour
If it’s night and the ISS is overhead, the script sends an email notification through Gmail’s SMTP server.


Email Notification
The script sends an alert using:
with smtplib.SMTP("smtp.gmail.com", port=587)
You must set:
MY_EMAIL
MY_PASSWORD
If using Gmail:
You must create an App Password because normal account passwords do not work with SMTP.
Requirements
Install dependencies with:
pip install requirements.txt
Also requires standard Python libraries:
smtplib
datetime
time
