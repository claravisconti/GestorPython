from leer_productos import leer_productos
from agregar_producto import agregar_producto
from buscar_producto import buscar_productos
from eliminar_producto import eliminar_producto
from actualizar_producto import actualizar_producto
from mostrar_reporte import mostrar_reporte
from conexion import crear_base, insertar_productos_si_vacia

crear_base() 
insertar_productos_si_vacia()

while True: 

    print("\nMenú de opciones:")
    print("1. Mostrar productos")
    print("2. Agregar producto")
    print("3. Buscar producto: ID, nombre o categoría")
    print("4. Eliminar producto")
    print("5. Actualizar producto")
    print("6. Reporte de productos que tengan una cantidad igual o inferior a un límite especificado por el usuario o usuaria.")
    print("7. Salir\n")
    
    opcion = input("Seleccione una opción: ")
        
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
        break
    elif opcion == "6":
        mostrar_reporte()
        break
    elif opcion == "7":
        print("Cierre de sesión exitoso")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del menú.")