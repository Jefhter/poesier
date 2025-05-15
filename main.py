!pip install google-genai

import os
from google.colab import userdata
from google import genai

os.environ['GOOGLE_API_KEY'] = userdata.get('GOOGLE_API_KEY')
client = genai.Client()
modelo = "gemini-2.0-flash"

def gerar_poema(palavra):
  requisicao = f"Imagine-se como um Compositor de Poemas. Preciso que vc faça um poema sobre: {palavra}"
  resposta = client.models.generate_content(model=modelo, contents=requisicao)
  return resposta.text

palavra = input("Digite uma palavra: ")
poema = gerar_poema(palavra)
print(f"Poema Gerado:\n\n{poema}")
