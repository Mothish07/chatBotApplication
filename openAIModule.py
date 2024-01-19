#Open API Module


from openai import OpenAI
import os
from kivy.clock import Clock

class OpenAIModule():
 
   def __init__(self):
      key = os.getenv("OPENAI_API_KEY")
      self.client = OpenAI(api_key= key)
      self.system_message = [{"role": "system", "content": "You are a kindly helpful friend."},]


   def generate_reply(self,user_input,update_chat_history):
      try:
         messages = self.system_message + [{"role": "user", "content": user_input}] 
         chat = self.client.chat.completions.create(model="gpt-3.5-turbo", messages=messages,callback=lambda x: Clock.schedule_once(lambda dt: update_chat_history(x.choices[0].message.content)))
      except Exception:
            update_chat_history("Something Went Wrong Please Try again!!")
      
"""
Example usage
   def send_message(self, instance):
        user_input = self.user_input.text
        if user_input:
            self.openai_module.generate_reply(user_input, self.update_chat_history)

    def update_chat_history(self, reply):
        self.chat_history.text += f'\nUser: {self.user_input.text}'
        self.chat_history.text += f'\nAI: {reply}'
        self.user_input.text = ''  # Clear user input

"""



