class vehiculo():
    color = "negro"
    ruedas = 4
    puertas = 5

class coche(vehiculo):
    velocidad = 210
    cilindrada = 4

ford  = coche()
print("el color es", coche().color)