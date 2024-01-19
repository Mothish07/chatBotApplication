# audio to text conveter module

import speech_recognition as sr
from kivy.clock import Clock
import threading

def audio_to_text(callback):
    def recognize_audio():
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=7)

        try:
            text = recognizer.recognize_google(audio)
            Clock.schedule_once(lambda dt:callback(text))
        except sr.UnknownValueError:
            Clock.schedule_once(lambda dt:callback("Cannot understand the audio..Please Try again"))
        except Exception:
            Clock.schedule_once(lambda dt:callback("Something Went Wrong Please Try again!!!"))
    threading.Thread(target=recognize_audio).start() # Threading allows for parallel execution, enabling the UI to continue updating and responding to user input while the audio recognition process is in progress.
"""
Example Usage
def audio_btn(self,instance):
 def callback(text):
            self.user_input.text = text

        audio_to_text(callback)
"""
     