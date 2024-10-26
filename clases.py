class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

     # Funcioones genericas internas en la clase
    def retornar_user(self):
        return f"Usuario:{self.nombre},edad:{self.edad}"


usuario_uno = Usuario("Jeremias", 23)

print(usuario_uno.retornar_user())
