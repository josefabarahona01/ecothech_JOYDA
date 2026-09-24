class Empleado:
    def __init__(self, nombre, correo, id=None):
        self.id = id
        self.nombre = nombre
        self.correo = correo

    def mostrar_datos(self):
        return "Nombre: " + self.nombre + ", Correo: " + self.correo

