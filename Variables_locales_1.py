# Variables locales Ej. 1

def contar_vocales(texto):
    vocales = "aeiouAEIOU"
    conteo = 0 # local
    for letra in texto:
        if letra in vocales:
            conteo += 1
    return conteo

text = input("Ingresa un texto para contar sus vocales: ")
total = contar_vocales(text)
print(f"Hay {total} vocales") 