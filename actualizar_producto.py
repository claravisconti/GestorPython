from conexion import conectar
from eliminar_producto import buscar_producto_pornombre
from agregar_producto import solicitar_datos

#     ELIMINAR PRODUCTO 
def actualizar_producto():

    #    Inicializar conn como None para manejar el cierre de conexión en el bloque finally
    conn = None
    #     TRY-EXCEPT-FINALLY: Intentar conectar a la base de datos y realizar la búsqued, mostrar errores y ejecutar el cierre de la conexión
    #     Usar un bloque try-except para manejar errores de conexión o consulta

    #   Buscar producto por nombre > devuelve un objeto producto
    producto_encontrado = buscar_producto_pornombre() 

    #   Pedir nuevos datos para actualizar el producto > devuelve nombre, descripción, cantidad, precio y categoría
    nuevos_datos = solicitar_datos() 
    
    try:
        conn = conectar()
        cursor = conn.cursor()
        #    Iniciar una transacción para asegurar la atomicidad de la operación
        cursor.execute('BEGIN TRANSACTION;')

    #    Ejecutar la consulta para insertar el producto
        cursor.execute('''
            UPDATE productos
            SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ?
            WHERE id = ?
        ''', (nuevos_datos[0], nuevos_datos[1],nuevos_datos[2],nuevos_datos[3], nuevos_datos[4], producto_encontrado[0]))

        #     Confirmar los cambios en la base de datos
        #     Usar commit() para guardar los cambios > Opción default de SQLite3
        conn.commit()
        print(f'\nProducto "{nuevos_datos[0]}" actualizado correctamente.')

    #    Manejar errores de conexión o consulta
    #    Si ocurre un error, hacer rollback para deshacer los cambios
    except Exception as e:
        if conn:
            conn.rollback()
        print(f'\nError al actualizar productos: {e}')

    finally:
        if conn:
            conn.close()