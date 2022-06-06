# Rain Alert

##### Table of Contents

- [Description](#description)
- [How To Use](#how-to-use)
- [References](#references)

---

## Description

This app will access the OpenWeather API and check to see if there will be precepitation in the user's area within the next 12 hours. If so, the app will send the user a text message notification to bring an umbrella

##### Controls

- Twilio account_sid and auth_token values would need to be updated to a user's account
- twilio_ph_num value should be set to a user's twilion account phone number
- receiver_ph_num value should be set to the recipient's phone number
    - twilio can only send texts to numbers verified by the account
- weather_params["lat"] and weather_params["lon"] values should be set to the location where the weather should be monitored

##### Technologies

- Python
- Twilio
- API requests
- Visual Studio

---

## How To Use

Download or clone this repository to your desktop. Run main.py in an appropriate Python environment.

---

## References

##### Continuing Work on

- https://github.com/SDBranka/_100DOP_Exercises

\
[Back To The Top](#rain-alert)