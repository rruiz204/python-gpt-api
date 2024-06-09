from openai import OpenAI
from config import config
from response import format_respones

openai_cfg = config["openai"]
client = OpenAI(api_key=openai_cfg.get("api_key"))

user_input = input("Ingrese un palabra: ")

def generate(word):
  prompt = f"genera 10 sinónimos y 10 antónimos de la palabra '{word}' en el siguiente formato:\n\nSinónimos:\n1. Sinonimo1\n...\n10. Sinonimo10\n\nAntónimos:\n1. Antonimo1\n...\n10. Antonimo10"

  completion = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{ "role": "user", "content": prompt }])

  sinonimos, antonimos = format_respones(completion.choices[0].message.content)

  print(sinonimos)
  print(antonimos)

generate(word=user_input)