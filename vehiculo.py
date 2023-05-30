import pickle

class vehiculo:
    def __init__(self, color, modelo):
        self.color = color
        self.modelo = modelo

    def __str__(self):
        return self.color + " " + self.modelo

ford = vehiculo("azul", "focus")
print(ford)

Vehiculo = open("claseVehiculo", 'wb')

pickle.dump(ford, Vehiculo)
nuevo_ford = __loader__
print(nuevo_ford)
Vehiculo.close()









Vehiculo.close()
