from conexion import conectar
from eliminar_producto import buscar_producto_pornombre
from agregar_producto import solicitar_datos
from colorama import init, Fore, Style

#     ELIMINAR PRODUCTO 
def actualizar_producto():
    conn = None

    producto_encontrado = buscar_producto_pornombre()
    if not producto_encontrado:
        print(Fore.RED + "Producto no encontrado.")
        return

    nuevos_datos = solicitar_datos()
    if len(nuevos_datos) < 5:
        print(Fore.RED + "Datos incompletos para actualizar el producto.")
        return

    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('BEGIN TRANSACTION;')

        cursor.execute('''
            UPDATE productos
            SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ?
            WHERE id = ?
        ''', (nuevos_datos[0], nuevos_datos[1], nuevos_datos[2], nuevos_datos[3], nuevos_datos[4], producto_encontrado[0]))

        conn.commit()
        print(Fore.GREEN + f'\nProducto "{nuevos_datos[0]}" actualizado correctamente.')

    except Exception as e:
        if conn:
            conn.rollback()
        print(Fore.RED + f'\nError al actualizar productos: {e}')

    finally:
        if conn:
            conn.close()
