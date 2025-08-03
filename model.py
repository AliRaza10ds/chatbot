# model.py

import google.generativeai as genai
from gtts import gTTS
import io
from dotenv import load_dotenv
import os


load_dotenv()

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"]=GOOGLE_API_KEY
genai.configure(api_key=GOOGLE_API_KEY)


def model(prompt):
    from google import genai
    client=genai.Client()
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=[{
            "role": "user",
            "parts": [{
                "text": prompt  
            }]
        }]
    )
    result=response.text
    return result
    

def text_to_speech(text, lang='en'):
    tts = gTTS(text, lang=lang)
    mp3_fp = io.BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    return mp3_fp