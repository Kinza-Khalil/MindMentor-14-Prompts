from typing import Any, Text, Dict, List
import openai
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class ActionMentalHealthAdvice(Action):
    def name(self) -> Text:
        return "action_mental_health_advice"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message['text']
        prompt = f"Please provide advice for someone with the following concern: {user_message}"
        response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=150, n=1, stop=None, temperature=0.7)
        generated_response = response.choices[0].text.strip()
        dispatcher.utter_message(text=generated_response)
        return []