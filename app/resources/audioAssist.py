from flask_restful import Resource
from flask import request, jsonify
from app.models.audio import procesar_audio  # Importa la función para procesar audio
import io
import tempfile
from pydub import AudioSegment 
import os
class MensajeAudio(Resource):
    def post(self):
        print("Solicitud post de la api de audio")

        # Lee el archivo de audio y conviértelo en un flujo de bytes
        file = request.files["file"]    
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        file.save(temp_file.name)

            # Procesar el archivo de audio
        transcripcion = procesar_audio(temp_file.name)
        
      
        # Retorna el texto de la transcripción
        return transcripcion
    
    