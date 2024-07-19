from flask_restful import Resource
from flask import request
from app.models.asistente import enviar_mensaje
from PIL import Image
import io


class AsistenteAI(Resource):
 def get(self):
        print("Solicitud get de la API asistente")
        
        return 
 def post(self):
        print("Solicitud post de la API asistente")
        data=request.get_json()
        
        mensaje=data['mensaje']
        respuesta=enviar_mensaje(mensaje)
      
        return respuesta