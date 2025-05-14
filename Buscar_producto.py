def buscarProductos(productos):
    busqueda = input("\nIngrese el nombre del producto: ")
    encontrado = False
    for producto in productos:
        if busqueda.lower() in producto["nombre"].lower():
            print(f"\nProducto: {producto['nombre']}")
            print(f"Categoría: {producto['categoria']}")
            print(f"Precio: {producto['precio']}")
            encontrado = True
            break
    if not encontrado:
        print("Producto no encontrado.")

