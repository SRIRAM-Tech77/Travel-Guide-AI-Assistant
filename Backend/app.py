from flask import Flask, request, jsonify
from google import genai
from flask_cors import CORS
import requests
import tempfile, base64
import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv(Path(__file__).resolve().parent / ".env")

MURF_API_KEY = os.getenv("MURF_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

PROMPTS = {
       "Summary": """
You are a professional tourist guide.
Provide a high-level overview of "{place}" in {language}.

Focus on:
- The historical significance
- Why the place is famous
- Key architectural or cultural highlights

Keep the explanation concise, engaging, and easy to follow.
Avoid excessive details and dates.
Limit the response to around 200 words.

Respond ONLY in {language}.
""",

    "Detailed": """
You are a professional tourist guide.
Provide a detailed and immersive explanation of "{place}" in {language}.

Cover:
- Historical background and timeline
- Architectural design and unique features
- Cultural importance and notable events
- Interesting facts and visitor insights

Explain concepts clearly and in a storytelling manner.
Include relevant details and examples to create a rich experience.
Limit the response to around 400 words.

Respond ONLY in {language}.
"""
}

app = Flask(__name__)
CORS(app)

Client = genai.Client(api_key= GEMINI_API_KEY)

def generate_speech(text, voice_id, locale):
        temp_file = tempfile.NamedTemporaryFile(suffix = ".mp3", delete=False)

        url = "https://global.api.murf.ai/v1/speech/stream"
        headers = {
            "api-key": MURF_API_KEY,
            "Content-Type": "application/json"
        }
        data = {
        "voice_id": voice_id,
        "style": "Conversational",
        "text": text,
        "locale": locale,
        "model": "falcon-2",
        "format": "MP3",
        "sampleRate": 24000,
        "channelType": "MONO"
        }

        response = requests.post(url, headers=headers, json=data, stream=True)

        if response.status_code == 200:
            with open(temp_file.name, "wb") as f:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
        else:
            print(f"Error: {response.status_code}")

        return temp_file.name
             
def generate_description(place, answer_type, language):
    prompt = PROMPTS [answer_type].format(place=place, language=language)
    response = Client.models.generate_content(
        model='gemini-3.5-flash-lite',
        contents=prompt
    )
    return response.text

@app.route('/generate-audio-guide', methods=['POST'])
def generate_audio_guide():
    data = request.json
    place =  data['place']
    answer_type = data['answerType']
    language = data['language']
    voice_id = data['voiceId']
    locale = data['locale']
    text_description = generate_description (place, answer_type, language)

    audio_path = generate_speech (text_description, voice_id, locale)

    audio_bytes = open(audio_path, "rb").read()
    encoded_audio = base64.b64encode(audio_bytes).decode('utf-8')

    return {"description": text_description, "audioBase64": encoded_audio}
    
app.run(debug=True)