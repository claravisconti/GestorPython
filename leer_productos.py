#Sin indices
#def leer_productos(productos):
    # for producto in productos:
    #     print(f"{producto['nombre']} - {producto['categoria']} - ${producto['precio']}")

#Con indices
# def leer_productos(productos):
#     for indice, producto in enumerate(productos):
#         print(f"{indice+1}: {producto['nombre']} - {producto['categoria']} - ${producto['precio']}")

# from conexion import conectar

# def leer_productos():
#     conn = conectar()
#     cursor = conn.cursor()

#     cursor.execute('SELECT * FROM productos')
#     productos = cursor.fetchall()

#     conn.close()

#     print(productos)

#     for producto in productos: 
#         print(f"ID: {producto[0]}, Nombre: {producto[1]}, Descripción: {producto[2]}, Cantidad: {producto[3]}, Precio: {producto[4]}, Categoría: {producto[5]}")

#     return productos

# leer_productos()

from conexion import conectar

def leer_productos():
    try:
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM productos')
        productos = cursor.fetchall()

        for producto in productos: 
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Descripción: {producto[2]}, Cantidad: {producto[3]}, Precio: {producto[4]}, Categoría: {producto[5]}")

        return productos

    except Exception as e:
        print(f"Error al leer productos: {e}")
        return []

    finally:
        if 'conn' in locals():
            conn.close()