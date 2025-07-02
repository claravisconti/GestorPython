# def agregarProductos(productos):

#     index = len(productos) + 1
#     # nombre = input("Ingrese el nombre del producto: ")
#     # categoria = input("Ingrese la categroría del producto: ")
#     # precio = int(input("Ingrese el precio del producto: "))

#     while True:
#         nombre = input("Ingrese el nombre del producto: ")
#         if nombre.replace(" ", "").isalpha():
#             break
#         else:
#             print("Error: El nombre debe contener solo letras y espacios.")

#     while True:
#         categoria = input("Ingrese la categoría del producto: ")
#         if categoria.replace(" ", "").isalpha():
#             break
#         else:
#             print("Error: La categoría debe contener solo letras y espacios.")

#     while True:
#         entrada = input("Ingrese el precio del producto: ")
#         try:
#             precio = int(entrada)
#             if precio >= 0:
#                 break
#             else:
#                 print("Error: El precio no puede ser negativo.")
#         except ValueError:
#             print("Error: Ingresá un número entero válido para el precio.")

#     nuevo_producto = {
#         "indice": index,
#         "nombre": nombre,
#         "categoria": categoria,
#         "precio": precio
#     }  

#     productos.append(nuevo_producto)         
#     print(f"\nProducto {nuevo_producto['nombre']} agregado correctamente.")

from conexion import conectar

#     SOLICITAR DATOS DEL PRODUCTO
def solicitar_datos():
    while True:
        nombre = input("Nombre del producto*: ").strip()
        if nombre:
            break
        print("El nombre no puede estar vacío.")

    descripcion = input("Descripción: ").strip()

    while True:
        cantidad = input("Cantidad*: ").strip()
        if cantidad.isdigit() and int(cantidad) >= 1:
            cantidad = int(cantidad)
            break
        print("Cantidad inválida. Debe ser un número mayor a 0")

    while True:
        precio = input("Precio*: ").strip()
        try:
            precio = float(precio)
            if precio >= 0:
                break
            else:
                print("Cantidad inválida. Debe ser un número mayor a 0")
        except ValueError:
            print("Precio inválido. Ingresá un número decimal.")

    while True:
        categoria = input("Categoría*: ").strip()
        if categoria:
            break
        print("La categoría no puede estar vacía.")

    return nombre, descripcion, cantidad, precio, categoria

#     AGREGAR EL PRODUCTO CON LOS DATOS SOLICITADOS
def agregar_producto():
    nombre, descripcion, cantidad, precio, categoria = solicitar_datos()

    conn = None
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('BEGIN TRANSACTION;')

        cursor.execute('''
            INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
            VALUES (?, ?, ?, ?, ?)
        ''', (nombre, descripcion, cantidad, precio, categoria))

        conn.commit()
        print(f'Producto "{nombre}" insertado correctamente.')

    except Exception as e:
        if conn:
            conn.rollback()
        print(f'Error al insertar producto: {e}')

    finally:
        if conn:
            conn.close()
