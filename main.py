import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
# in your environment, in Bash terminal use:
# export name_of_variable_to_store
# to store that information outside of your cody body
# api_key = "Your API KEY HERE"
api_key = os.environ.get("OWM_API_KEY")
account_sid = "1AC7c357bb2c78d78979800071781270f39"
auth_token = os.environ.get("AUTH_TOKEN")
twilio_ph_num = "+12057362422"
# twilio can only send texts to numbers verified by the account
receiver_ph_num = "+13066346733"


weather_params = {
    "lat": 51.507351,
    "lon": -0.127758,
    "exclude": "current,minutely,daily",
    "appid": api_key
}

response = requests.get(OWM_Endpoint, params=weather_params)
# print(response.status_code)
response.raise_for_status()
# print(response.json())
response = requests.get(OWM_Endpoint, params=weather_params)
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
# print(weather_slice)

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    # create proxy client in order to run app from cloud service PythonAnywhere
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    # create twilio client
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_=twilio_ph_num,
        to=receiver_ph_num
    )
    print(message.status)
