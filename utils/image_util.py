import requests
from PIL import Image
from io import BytesIO

def carregar_imagem(url, tamanho=(150, 150)):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img = img.resize(tamanho)
    bio = BytesIO()
    img.save(bio, format="PNG")
    return bio.getvalue()