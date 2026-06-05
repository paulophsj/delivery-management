import requests
from PIL import Image
from io import BytesIO

def carregar_imagem(url, tamanho=(150, 150)):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content))
    except Exception:
        img = Image.new("RGB", tamanho, color="#C2D4D6")

    img = img.resize(tamanho)
    bio = BytesIO()
    img.save(bio, format="PNG")
    return bio.getvalue()
