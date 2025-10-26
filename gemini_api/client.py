from google import genai
from decouple import config


def get_car_ai_bio(model, brand, year):
    # 🔑 Passe sua chave diretamente aqui
    client = genai.Client(api_key=config("GEMINI_API_KEY"))

    prompt = (
        f"Crie uma descrição de venda para o carro {brand} {model} {year} "
        f"em no máximo 250 caracteres. Fale coisas específicas sobre o modelo, descreva especificações técnicas desse modelo de carro."
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text.strip()
