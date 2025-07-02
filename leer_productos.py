from conexion import conectar

#     MOSTRAR TODOS LOS PRODUCTOS

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


#     MOSTRAR PRODUCTOS ESPECIFICOS

def mostrar_productos(productos):
    if not productos:
        print("\nNo se encontraron productos.")
        return

    print("\nResultados encontrados:")
    for producto in productos:
        print(f"ID: {producto[0]}")
        print(f"Nombre: {producto[1]}")
        print(f"Descripción: {producto[2]}")
        print(f"Cantidad: {producto[3]}")
        print(f"Precio: ${producto[4]:.2f}")
        print(f"Categoría: {producto[5]}")
