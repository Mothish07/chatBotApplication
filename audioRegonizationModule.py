# audio to text conveter module

import speech_recognition as sr

def audio_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
       print("Start Getting Input")
       recognizer.adjust_for_ambient_noise(source)
       audio = recognizer.listen(source, timeout=7)

    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Audio data has been not getted!!")
        return "Cannot Understand the Audio Try Again "
    except sr.RequestError as e:
        print(f"Could not request results from Google Web Speech API; {e}")
        return "Network Issue ! Please check your  Internet connection"
