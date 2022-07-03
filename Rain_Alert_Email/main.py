import requests
import smtplib
API_KEY = "a17d56d787efe1f2ab5c6eab0f96a5ae"
parameters = {
    "lat": 52.165935,
    "lon": 21.015220,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}
my_email = "your_email@gmail.com"
password = "your_password"
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="your_email@outlook.com",
                            msg=f"Subject: 🌧️ RAIN ALERT 🌧️ \n\n Be careful, rain is on the way!")

