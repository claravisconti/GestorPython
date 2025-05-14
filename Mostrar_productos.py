#Sin indices
#def mostrarProductos(productos):
    # for producto in productos:
    #     print(f"{producto['nombre']} - {producto['categoria']} - ${producto['precio']}")

#Con indices
def mostrarProductos(productos):
    for indice, producto in enumerate(productos):
        print(f"{indice+1}: {producto['nombre']} - {producto['categoria']} - ${producto['precio']}")