# Crea runa lista de palabras
palabras = input("ingrese las palabras para filtrar").lower().split()

def empieza_por_letra(palabra, letra):
  return palabra .startswith(letra)

palabras_filtradas = [p for p in palabras if p.startswith("c")]

print(palabras_filtradas)