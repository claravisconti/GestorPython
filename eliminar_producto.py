from conexion import conectar

#     SOLICITAR DATOS DEL PRODUCTO A BUSCAR
def buscar_producto_pornombre():

    #     Lista para almacenar los productos encontrados
    producto = []
    #    Inicializar conn como None para manejar el cierre de conexión en el bloque finally
    conn = None
    #     TRY-EXCEPT-FINALLY: Intentar conectar a la base de datos y realizar la búsqued, mostrar errores y ejecutar el cierre de la conexión
    #     Usar un bloque try-except para manejar errores de conexión o consulta
    try:
        conn = conectar()
        cursor = conn.cursor()

        nombre_buscar = input("Ingresá el nombre: ").strip()
        cursor.execute('SELECT * FROM productos WHERE UPPER(nombre) = ?', (nombre_buscar.upper(),))
        productos = cursor.fetchall()

        if not productos:
            print("\nNo se encontraron productos con esa categoría.")
            return []
        print("\nResultados encontrados:")

        #   Mostrar los detalles del producto encontrado
        for producto in productos:
            print(f"\nID: {producto[0]}, Nombre: {producto[1]}, Descripción: {producto[2]}, Cantidad: {producto[3]}, Precio: ${producto[4]:.2f}, Categoría: {producto[5]}")

        return producto

    except Exception as e:
        print(f'\nError en la búsqueda: {e}')
        return []

    finally:
        if conn:
            conn.close()

#     ELIMINAR PRODUCTO 
def eliminar_producto():

    #    Inicializar conn como None para manejar el cierre de conexión en el bloque finally
    conn = None
    #     TRY-EXCEPT-FINALLY: Intentar conectar a la base de datos y realizar la búsqued, mostrar errores y ejecutar el cierre de la conexión
    #     Usar un bloque try-except para manejar errores de conexión o consulta

    #   Desestructurar el producto a eliminar
    producto = buscar_producto_pornombre()
    
    try:
        conn = conectar()
        cursor = conn.cursor()
        #    Iniciar una transacción para asegurar la atomicidad de la operación
        cursor.execute('BEGIN TRANSACTION;')
    #    Ejecutar la consulta para insertar el producto
        cursor.execute('DELETE FROM productos WHERE id = ?', (producto[0],))
        if cursor.rowcount == 0:
            print(f"⚠️ No se encontró ningún producto con ID {producto[0]}.")
            conn.rollback()
            return
        #     Confirmar los cambios en la base de datos
        #     Usar commit() para guardar los cambios > Opción default de SQLite3
        conn.commit()
        print(f'\nProducto "{producto[1]}" eliminado correctamente.')

    #    Manejar errores de conexión o consulta
    #    Si ocurre un error, hacer rollback para deshacer los cambios
    except Exception as e:
        if conn:
            conn.rollback()
        print(f'\nError al eliminar productos: {e}')

    finally:
        if conn:
            conn.close()