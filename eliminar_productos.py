from conexion import conectar

def buscar_producto_pornombre():
    conn = None
    try:
        conn = conectar()
        cursor = conn.cursor()

        nombre_buscar = input("Ingresá parte del nombre del producto: ").strip()
        cursor.execute('SELECT * FROM productos WHERE UPPER(nombre) LIKE ?', ('%' + nombre_buscar.upper() + '%',))
        productos = cursor.fetchall()

        if not productos:
            print("\nNo se encontraron productos con ese nombre.")
            return None

        print("\nResultados encontrados:")
        for producto in productos:
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Descripción: {producto[2]}, Cantidad: {producto[3]}, Precio: ${producto[4]:.2f}, Categoría: {producto[5]}")

        if len(productos) > 1:
            id_seleccionado = input("\nIngresá el ID del producto que querés eliminar: ").strip()
            if not id_seleccionado.isdigit():
                print("El ID debe ser un número entero.")
                return None

            id_seleccionado = int(id_seleccionado)
            for producto in productos:
                if producto[0] == id_seleccionado:
                    return producto  #  Devuelve la tupla (producto seleccionado)

            print("No se encontró un producto con ese ID.")
            return None

        else:
            return productos[0]  # Si solo hay un producto, lo devuelve directamente

    except Exception as e:
        print(f'Error en la búsqueda: {e}')
        return None

    finally:
        if conn:
            conn.close()

def eliminar_producto():
    producto = buscar_producto_pornombre()

    if not producto:
        print("⚠️ No se seleccionó ningún producto para eliminar.")
        return

    conn = None
    try:
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute('BEGIN TRANSACTION;')
        cursor.execute('DELETE FROM productos WHERE id = ?', (producto[0],))

        if cursor.rowcount == 0:
            print(f"⚠️ No se encontró ningún producto con ID {producto[0]}.")
            conn.rollback()
            return

        conn.commit()
        print(f' Producto "{producto[1]}" eliminado correctamente.')


    except Exception as e:
        if conn:
            conn.rollback()
        print(f'Error al eliminar producto: {e}')

    finally:
        if conn:
            conn.close()

