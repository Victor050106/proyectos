# Crear una lista de palabras
palabras = ("hola", "adios", "casa", "perro", "gato", "coche","roberto carlos","coca Cola")

def empieza_por_letra(palabra, letra):
  return palabra.startswith(letra)

palabras_filtradas = list(filter(lambda x: empieza_por_letra(x, "c"), palabras))

print(palabras_filtradas)