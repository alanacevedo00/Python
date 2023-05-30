class alumno():
    nombre = "rodolfo"
    nota = 5

alu = alumno()
if alumno.nota>=7:
    print("el alumno",alumno.nombre, "obtuvo un", alumno.nota, "y su estado es aprobado")
else:
    print("el alumno",alumno.nombre, "obtuvo un", alumno.nota, "y su estado es desaprobado")