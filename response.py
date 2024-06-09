import re

def format_respones(content):
  sinonimos = re.findall(r'\b[A-Za-záéíóúüÁÉÍÓÚÜ]+\b', re.search(r'Sinónimos:(.*?)Antónimos:', content, re.S).group(1))
  antonimos = re.findall(r'\b[A-Za-záéíóúüÁÉÍÓÚÜ]+\b', re.search(r'Antónimos:(.*)', content, re.S).group(1))
  return sinonimos, antonimos