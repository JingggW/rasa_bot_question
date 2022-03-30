# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, SessionStarted, ActionExecuted, EventType
from rasa_sdk.executor import CollectingDispatcher
import csv
import pandas as pd
#
#
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_save_conv"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        conversation = tracker.events
        event = []
        timestamp = []
        text = []
        intent = []
        confidence = []

        for i in conversation:
          if i['event'] == 'action':
            event.append(i['event'])
            timestamp.append(i['timestamp'])
            intent.append(i['name'])
            confidence.append(i['confidence'])
            text.append('')
          if i['event'] == 'user':
            event.append(i['event'])
            text.append(i['text'])
            timestamp.append(i['timestamp'])
            intent.append(i['parse_data']['intent']['name'])
            confidence.append(i['parse_data']['intent']['confidence'])
          if i['event'] == 'bot':
            event.append(i['event'])
            timestamp.append(i['timestamp'])
            text.append(i['text'])
            intent.append('')
            confidence.append('')

        d = {'event': event, 'timestamp': timestamp, 'intent': intent, 'text': text, 'confidence': confidence}
        df = pd.DataFrame(data=d)
        df.to_csv('conv_logs.csv')

        dispatcher.utter_message(text="Hello World!")

        return []


#class ActionSessionStart(Action):
#    def name(self) -> Text:
#        return "action_session_start"

#    async def run(
#      self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
#    ) -> List[Dict[Text, Any]]:

        # the session should begin with a `session_started` event
 #       events = [SessionStarted()]

        # any slots that should be carried over should come after the
        # `session_started` event
        # events.extend(self.fetch_slots(tracker))
#        dispatcher.utter_message(text="Hello")
#        dispatcher.utter_message(text="Hola, I'm your question bot! Ask me a question!")
        # an `action_listen` should be added at the end as a user message follows
#        events.append(ActionExecuted("action_listen"))

#        return events
