from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config["SECRET"] = "ajuiahfa78fh9f78shfs768fgs7f6"
app.config["DEBUG"] = True
socketio = SocketIO(app, cors_allowed_origins="*")

# Importe a biblioteca do chatbot aqui
import google.generativeai as genai

# Configurações do chatbot
GOOGLE_API_KEY = "CHAVE API"
genai.configure(api_key=GOOGLE_API_KEY)

generation_config = {
  "candidate_count": 1,
  "temperature": 0.5,
}

safety_settings = {
    'HATE': 'BLOCK_NONE',
    'HARASSMENT': 'BLOCK_NONE',
    'SEXUAL': 'BLOCK_NONE',
    'DANGEROUS': 'BLOCK_NONE'
}
