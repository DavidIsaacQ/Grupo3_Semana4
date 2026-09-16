def funcion_a():
    valor = 100          
    return valor
def funcion_b():
    valor = 200          
    return valor
# local a funcion_a
# local a funcion_b (independiente)
print(funcion_a(), funcion_b())  # 100  200