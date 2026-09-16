#Variables Globales Ejemplo 1
visitas = 0    #global
def registrar_visitas():
    global visitas
    visitas += 1
    print(f"Visita #{visitas} registrada")

registrar_visitas()  #visitas #1
registrar_visitas()   #visitas #2
print(f"total:{visitas} ")    #total: 2