def eliminarProductos(productos):
    busqueda = input("\nIngrese el nombre del producto: ")
    for producto in productos:
        if busqueda.lower() in producto["nombre"].lower():
            productos.remove(producto)
            print(f"Producto '{producto['nombre']}' eliminado exitosamente.")
            break 
        else:
            print("Producto no encontrado.")
            break  