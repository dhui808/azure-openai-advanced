import azure.cognitiveservices.speech as speechsdk
import os
from dotenv import load_dotenv
load_dotenv()

speech_key, service_region = os.getenv('SPEECH_SERVICE_KEY'), "EastUS"

speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

# Creates an audio configuration that points to an audio file
audio_config = speechsdk.audio.AudioConfig(filename="./TedTalk_Bill_Gates.wav")

# Creates a recognizer with the given settings
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

print("Recognizing speech from file...")
result = speech_recognizer.recognize_once()

# Prints the recognized text
print("recognized text=" + result.text)


