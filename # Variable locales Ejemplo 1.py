# Variable locales Ejemplo 1

def contar_vocales(texto):
    vocales = "aeiouAEIOU"
    conteo = 0   # Local
    for letra in texto:
        if letra in vocales:
            conteo += 1

    return conteo
print(contar_vocales("Hola Mundo"))  #4
       