from openai import OpenAI
import io
import os
client = OpenAI(
  organization='org-mZE8a7Qj1jjTBeTDLY1ecJ3C',
  project='proj_lsdxQWDy02Q24C1obcsrvUNA',
  api_key="sk-proj-hj8MJiZj9o0w30KmmjfxT3BlbkFJ8m79aosvJ7jqAnFWWNJ1"
)

def procesar_audio(archivo):
    audio_file = open(archivo, "rb")
    transcript = client.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file
    )
    transcripcion=transcript.text
    
    
    return transcripcion