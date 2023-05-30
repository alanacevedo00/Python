import sqlite3


conexion = sqlite3.connect('BasedeDatos.db')
cursorBD = conexion.cursor()
cursorBD.execute(""" CREATE TABLE IF NOT EXISTS alumno (
    codigo INTEGER, nombre TEXT, apellido TEXT)""")

cursorBD.execute("INSERT INTO alumno VALUES ('001','alan','acevedo')")
cursorBD.execute("INSERT INTO alumno VALUES ('002','luciano','montoya')")
cursorBD.execute("INSERT INTO alumno VALUES ('003','federico','ortega')")
cursorBD.execute("INSERT INTO alumno VALUES ('004','leonel','rey')")
cursorBD.execute("INSERT INTO alumno VALUES ('005','cristian','martinez')")
cursorBD.execute("INSERT INTO alumno VALUES ('006','sergio','serrillo')")
cursorBD.execute("INSERT INTO alumno VALUES ('007','diego','jesus')")
cursorBD.execute("INSERT INTO alumno VALUES ('008','claudio','sanches')")
conexion.commit()

cursorBD.execute("SELECT * FROM alumno")
InfoAlumno = cursorBD.fetchone()
print(InfoAlumno)

conexion.close()




if __name__ == "__main__":
    pass
