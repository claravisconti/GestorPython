def agregarProductos(productos):

    index = len(productos) + 1
    # nombre = input("Ingrese el nombre del producto: ")
    # categoria = input("Ingrese la categroría del producto: ")
    # precio = int(input("Ingrese el precio del producto: "))

    while True:
        nombre = input("Ingrese el nombre del producto: ")
        if nombre.replace(" ", "").isalpha():
            break
        else:
            print("Error: El nombre debe contener solo letras y espacios.")

    while True:
        categoria = input("Ingrese la categoría del producto: ")
        if categoria.replace(" ", "").isalpha():
            break
        else:
            print("Error: La categoría debe contener solo letras y espacios.")

    while True:
        entrada = input("Ingrese el precio del producto: ")
        try:
            precio = int(entrada)
            if precio >= 0:
                break
            else:
                print("Error: El precio no puede ser negativo.")
        except ValueError:
            print("Error: Ingresá un número entero válido para el precio.")

    nuevo_producto = {
        "indice": index,
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio
    }  

    productos.append(nuevo_producto)         
    print(f"\nProducto {nuevo_producto['nombre']} agregado correctamente.")
