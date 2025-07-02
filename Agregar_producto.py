from conexion import conectar
from leer_productos import leer_productos

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

        leer_productos()

    except Exception as e:
        if conn:
            conn.rollback()
        print(f'Error al insertar producto: {e}')

    finally:
        if conn:
            conn.close()
