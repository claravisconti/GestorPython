from conexion import conectar
from leer_productos import mostrar_productos
from colorama import init, Fore, Style

#     SOLICITAR DATOS DEL PRODUCTO A BUSCAR
def buscar_producto_pornombre():
    conn = None
    try:
        conn = conectar()
        cursor = conn.cursor()

        nombre_buscar = input("Ingresá el nombre: ").strip()
        cursor.execute('SELECT * FROM productos WHERE UPPER(nombre) = ?', (nombre_buscar.upper(),))
        productos = cursor.fetchall()

        if not productos:
            print(Fore.RED + "\nNo se encontraron productos con ese nombre.")
            return []

        producto = productos[0]

        mostrar_productos([producto])

        return producto

    except Exception as e:
        print(Fore.RED + f'\nError en la búsqueda: {e}')
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
            print(Fore.RED + f"No se encontró ningún producto con ID {producto[0]}.")
            conn.rollback()
            return
        #     Confirmar los cambios en la base de datos
        #     Usar commit() para guardar los cambios > Opción default de SQLite3
        conn.commit()
        print(Fore.GREEN + f'\nProducto "{producto[1]}" eliminado correctamente.')

    #    Manejar errores de conexión o consulta
    #    Si ocurre un error, hacer rollback para deshacer los cambios
    except Exception as e:
        if conn:
            conn.rollback()
        print(Fore.RED +f'\nError al eliminar productos: {e}')

    finally:
        if conn:
            conn.close()