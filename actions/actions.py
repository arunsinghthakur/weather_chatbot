# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "ActionCheckWeather"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
import requests


class ActionCheckWeather(Action):

    def name(self) -> Text:
        return "action_get_weather"

    def run(self, dispatcher, tracker, domain):

       api_key = 'Your API Key'
       loc = tracker.get_slot('location')
       current = requests.get('http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(loc, api_key)).json()
       print(current)
       country = current['sys']['country']
       city = current['name']
       condition = current['weather'][0]['main'    ]
       temperature_c = current['main']['temp']
       humidity = current['main']['humidity']
       wind_mph = current['wind']['speed']
       response = """It is currently {} in {} at the moment. The temperature is {} degrees, the humidity is {}% and the wind speed is {} mph.""".format(condition, city, temperature_c, humidity, wind_mph)
       dispatcher.utter_message(response)
       return [SlotSet('location', loc)]

        
