#Open API Module


from openai import OpenAI
import os

class OpenAIModule():
 
   def __init__(self):
      key = os.getenv("OPENAI_API_KEY")
      self.client = OpenAI(api_key= key)
      self.system_message = [{"role": "system", "content": "You are a kindly helpful friend."},]


   def generate_reply(self,user_input):
      
      try:
         messages = self.system_message + [{"role": "user", "content": user_input}] 
         chat = self.client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
         output = chat.choices[0].message.content  
         return output
      except Exception as error:
         output_error = "Error occured !..."
         return output_error
      




