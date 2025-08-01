import azure.cognitiveservices.speech as speechsdk
import os
from dotenv import load_dotenv
load_dotenv()

speech_key, service_region = os.getenv('SPEECH_SERVICE_KEY'), "EastUS"

speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

text = "Why do programmers always mix up Halloween and Christmas? Because Oct 31 equals Dec 25."

result = speech_synthesizer.speak_text_async(text).get()

if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Speech synthesized to speaker for text [{}]".format(text))
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        if cancellation_details.error_details:
            print("Error details: {}".format(cancellation_details.error_details))
    print("Did you update the subscription info?")

