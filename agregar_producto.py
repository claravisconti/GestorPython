from conexion import conectar
from leer_productos import leer_productos
from colorama import init, Fore, Style

#     SOLICITAR DATOS DEL PRODUCTO
def solicitar_datos():

    #   Usar while para validar que la categoría no esté vacía
    #   Solicitar datos del producto al usuario
    #   Usar un bucle while para asegurarse de que el nombre no esté vacío
    #   Usar strip() para eliminar espacios en blanco al inicio y al final
    while True:
        nombre = input("Nombre del producto*: ").strip()
        #   Validar que el nombre no esté vacío
        #   Si el nombre está vacío, mostrar un mensaje de error y volver a solicitar el nombre
        if nombre:
            break
        print(Fore.RED +"El nombre no puede estar vacío.")

    descripcion = input("Descripción: ").strip()

     #  Usar while para validar que la categoría no esté vacía
    #   Validar que la cantidad sea un número entero mayor a 0
    #   Usar un bucle while para asegurarse de que la cantidad sea mayor a 0
    #   Usar isdigit() para verificar si la entrada es un número entero
    #   Usar strip() para eliminar espacios en blanco al inicio y al final
    while True:
        cantidad = input("Cantidad*: ").strip()
        if cantidad.isdigit() and int(cantidad) >= 1:
            cantidad = int(cantidad)
            break
        print(Fore.RED +"Cantidad inválida. Debe ser un número mayor a 0")

    #  Usar while para validar que la categoría no esté vacía
    #   Validar que el precio sea un número decimal mayor a 0
    #   Usar strip() para eliminar espacios en blanco al inicio y al final
    while True:
        precio = input("Precio*: ").strip()
        try:
            precio = float(precio)
            if precio >= 0:
                break
            else:
                print(Fore.RED +"Cantidad inválida. Debe ser un número mayor a 0")
        except ValueError:
            print(Fore.RED +"Precio inválido. Ingresá un número decimal.")

    #  Usar while para validar que la categoría no esté vacía
    #  Usar strip() para eliminar espacios en blanco al inicio y al final
    while True:
        categoria = input("Categoría*: ").strip()
        if categoria:
            break
        print(Fore.RED +"La categoría no puede estar vacía.")

    return nombre, descripcion, cantidad, precio, categoria

#     AGREGAR EL PRODUCTO CON LOS DATOS SOLICITADOS
def agregar_producto():
    nombre, descripcion, cantidad, precio, categoria = solicitar_datos()
     
    #    Inicializar conn como None para manejar el cierre de conexión en el bloque finally
    conn = None
    #     TRY-EXCEPT-FINALLY: Intentar conectar a la base de datos y realizar la búsqued, mostrar errores y ejecutar el cierre de la conexión
    #     Usar un bloque try-except para manejar errores de conexión o consulta
    try:
        conn = conectar()
        cursor = conn.cursor()
        #    Iniciar una transacción para asegurar la atomicidad de la operación
        cursor.execute('BEGIN TRANSACTION;')
    #    Ejecutar la consulta para insertar el producto
        cursor.execute('''
            INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
            VALUES (?, ?, ?, ?, ?)
        ''', (nombre, descripcion, cantidad, precio, categoria))
        #     Confirmar los cambios en la base de datos
        #     Usar commit() para guardar los cambios > Opción default de SQLite3
        conn.commit()
        print(Fore.GREEN +f'Producto "{nombre}" insertado correctamente.')

        #     Llamar a la función leer_productos para mostrar los productos actualizados
        leer_productos()

    #    Manejar errores de conexión o consulta
    #    Si ocurre un error, hacer rollback para deshacer los cambios
    except Exception as e:
        if conn:
            conn.rollback()
        print(Fore.RED + f'Error al insertar producto: {e}')

    finally:
        if conn:
            conn.close()
