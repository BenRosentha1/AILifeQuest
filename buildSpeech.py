from warnings import catch_warnings, filterwarnings
from openai import OpenAI
from getAPI import getAPI
from pathlib import Path

# Use the API key in OpenAI client initialization
client = OpenAI(api_key=getAPI())

def buildSpeech(text, speed=1):
    speech_file_path = Path(__file__).parent / "speech.mp3"
    response = client.audio.speech.create(
        model="tts-1",
        voice="fable",
        input=text,
        speed=speed
    )

    # Suppress DeprecationWarning for response.stream_to_file
    with catch_warnings():
        filterwarnings("ignore", category=DeprecationWarning)
        try:
            response.stream_to_file(speech_file_path)  # Use speech_file_path instead of mp3_file_path
        except Exception as e:
            pass

    # return audio location
    return "C:/Users/benmr/OneDrive/Documents/Programming/AILifeQuest/AILifeQuest/speech.mp3"       # Undo this hardcoding later, implementation was not working without the hardcoded version
