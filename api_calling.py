
from google import genai
from dotenv import load_dotenv
import os
from gtts import gTTS
import io


#

load_dotenv()

api_key= os.getenv("GEMINI_API")
client = genai.Client(api_key = api_key)

def note_generator(images):
    promt = """Summarize the picture in note formate at max 10 words,
    make sure to add necessary markdown to differeciate section"""
    response = client.models.generate_content(
       model="gemini-3-flash-preview", 
       contents=[images,promt]
    )
    return response.text


def audio_transcription(text) :
    spech = gTTS(text , lang = 'en' , slow = False)
    audio_buffer = io.BytesIO()
    spech.write_to_fp(audio_buffer)
    return audio_buffer
def quizz_generator(images,difficulty):
    promt = f"""Germerte 3 quizz based on the {difficulty} , make sure to add markdown"""
    response = client.models.generate_content(
       model="gemini-3-flash-preview", 
       contents=[images,promt]
    )
    return response.text


