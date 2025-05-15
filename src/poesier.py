import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")
MODEL_NAME = "gemini-2.0-flash"

if not API_KEY:
    raise EnvironmentError("API key not found. Please add it to your .env file.")

client = genai.Client()

def gerar_poema(palavra):
    requisicao = f"Imagine-se como um Compositor de Poemas. Preciso que você faça um poema sobre: {palavra}"
    resposta = client.models.generate_content(model=MODEL_NAME, contents=requisicao)
    return resposta.text
