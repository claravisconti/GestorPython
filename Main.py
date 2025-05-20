from Login import login
from Productos import productos
from Mostrar_productos import mostrarProductos
from Agregar_producto import agregarProductos
from Buscar_producto import buscarProductos
from Eliminar_producto import eliminarProductos

login()

while True: 

    print("\nMenú de opciones:")
    print("1. Mostrar productos")
    print("2. Agregar producto")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir\n")
    
    opcion = input("Seleccione una opción: ")
        
    # if opcion == "1":
    #     mostrarProductos(productos)
    # elif opcion == "2":
    #     agregarProductos(productos)
    #     mostrarProductos(productos)
    # elif opcion == "3":
    #     buscarProductos(productos)
    # elif opcion == "4":
    #     eliminarProductos(productos)
    #     mostrarProductos(productos)
    # elif opcion == "5":
    #     print("Cierre de sesión exitoso")
    #     break
    # else:
    #     print("Opción no válida. Por favor, seleccione una opción del menú.")

    match opcion:
        case "1":
            mostrarProductos(productos)
        case "2":
            agregarProductos(productos)
            mostrarProductos(productos)
        case "3":
            buscarProductos(productos)
        case "4":
            eliminarProductos(productos)
            mostrarProductos(productos)
        case "5":
            print("Cierre de sesión exitoso")
            break
        case _:
            print("Opción no válida. Por favor, seleccione una opción del menú.")