from conexion import conectar

def actualizar_producto():
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