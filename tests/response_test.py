data_api = """
Sinónimos:
1. Veloz
2. Ágil
3. Pronto
4. Ligero
5. Acelerado
6. Veloz
7. Raudo
8. Presuroso
9. Fugaz
10. Corredizo

Antónimos:
1. Lento
2. Retardado
3. Pausado
4. Tardo
5. Moroso
6. Pesado
7. Despacio
8. Tardío
9. Languideciente
10. Tranquilo
"""
from response import format_respones

def test_lol():
  sinonimos, antonimos = format_respones(data_api)

  assert len(sinonimos) == 10
  assert len(antonimos) == 10