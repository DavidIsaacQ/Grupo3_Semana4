# Encapsulamiento en Python - Ej. 2

class Temperatura:
    def __init__(self, celsius=0):
        self._celsius = celsius
    @property
    def celsius(self):
        return self._celsius
    @celsius.setter
    def celsius(self, valor):
        if valor < -273.15:
            raise ValueError("Bajo cero absoluto")
        self._celsius = valor
t = Temperatura()
t.celsius = 25
print(t.celsius) # 25