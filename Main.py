from leer_productos import leer_productos
from agregar_producto import agregar_producto
from buscar_producto import buscar_productos
from eliminar_producto import eliminar_producto
from actualizar_producto import actualizar_producto
from mostrar_reporte import mostrar_reporte
from conexion import crear_base, insertar_productos_si_vacia
from colorama import init, Fore, Style

# Se inicializa la base de datos y se añaden productos si la base de datos está vacía.
crear_base() 
insertar_productos_si_vacia()

# Iniciar colorama para usar colores en la terminal
init(autoreset=True) 

while True: 

    print(Style.BRIGHT + "\nMenú de opciones:" + Style.RESET_ALL)
    print("1. Mostrar productos")
    print("2. Agregar producto")
    print("3. Buscar producto: ID, nombre o categoría")
    print("4. Eliminar producto")
    print("5. Actualizar producto")
    print("6. Filtrar productos por cantidad")
    print("7. Salir\n")
    
    opcion = input(Style.BRIGHT + "Seleccione una opción: "+ Style.RESET_ALL)
        
    if opcion == "1":
        leer_productos()
    elif opcion == "2":
        agregar_producto()
    elif opcion == "3":
        buscar_productos()
    elif opcion == "4":
        eliminar_producto()
    elif opcion == "5":
        actualizar_producto()
    elif opcion == "6":
        mostrar_reporte()
    elif opcion == "7":
        print(Fore.GREEN + "\nCierre de sesión exitoso")
        break
    else:
        print(Fore.RED + "\nOpción no válida. Por favor, seleccione una opción del menú.")