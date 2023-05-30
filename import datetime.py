import datetime

fechaActual = datetime.date.today()
print(fechaActual)

horaActual = datetime.datetime.now()
if horaActual.hour > 7 :
    print("Ya nos fuimos del trabajo :D ")
else:
    hora = time(19, 0, 0)
    diferencia = hora - horaActual.hour
    print("Faltan estas horas para irnos: ", diferencia)

