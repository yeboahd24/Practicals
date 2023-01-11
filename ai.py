import speech_recognition as sr
import pyttsx3
import openai
import json


openai.api_key = ""


def handle_voice_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        return text
    except:
        print("Sorry, I didn't understand that.")
        return None


def send_text_to_api(text):
    response = openai.Completion.create(engine="davinci", prompt=text, max_tokens=1024)
    return json.loads(response.text)


def parse_response(response):
    return response["response"]


def handle_text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


while True:
    input_text = handle_voice_input()
    if input_text is not None:
        response_json = send_text_to_api(input_text)
        response_text = parse_response(response_json)
        handle_text_to_speech(response_text)
    else:
        handle_text_to_speech(
            "I'm sorry, I didn't understand that. Could you please repeat your question?"
        )
