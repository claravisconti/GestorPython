from Usuarios import usuarios
import getpass

def login():
    while True:
        nombre = input("Ingrese su nombre de usuario: ")
        contraseña = getpass.getpass("Ingrese su contraseña: ")
        usuario_encontrado = False
        for usuario in usuarios:
            if usuario["nombre"] == nombre and str(usuario["contraseña"]) == contraseña:
                print(f"\n¡Hola, {nombre}!")
                usuario_encontrado = True
                break
        if usuario_encontrado:
            break
        else:
            print("Usuario y/o contraseña incorrectos.")