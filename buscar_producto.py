from conexion import conectar
from leer_productos import mostrar_productos
from colorama import init, Fore, Style

def buscar_productos():
    #       Menu de busquedas
    print("\nOpciones de búsqueda:")
    print("1. Buscar por ID")
    print("2. Buscar por Nombre")
    print("3. Buscar por Categoría")
    opcion = input("Elegí una opción: ")

    #     Lista para almacenar los productos encontrados
    productos = []

    #    Inicializar conn como None para manejar el cierre de conexión en el bloque finally
    conn = None

    #     TRY-EXCEPT-FINALLY: Intentar conectar a la base de datos y realizar la búsqued, mostrar errores y ejecutar el cierre de la conexión
    #     Usar un bloque try-except para manejar errores de conexión o consulta
    try:
        conn = conectar()
        cursor = conn.cursor()

        #     Dependiendo de la opción elegida, realizar la búsqueda correspondiente

        if opcion == '1':
            id_buscar = input(Style.BRIGHT +"Ingresá el ID del producto: ").strip()
            #     Validar que el ID sea un número entero
            #     Si no es un número entero, mostrar un mensaje de error y retornar una lista vacía
            if not id_buscar.isdigit():
                print(Fore.RED +"El ID debe ser un número entero.")
                return []
            #     Ejecutar la consulta para buscar por ID
            #     Usar ? para evitar inyecciones SQL
            #     Convertir id_buscar a entero para evitar errores de tipo
            cursor.execute('SELECT * FROM productos WHERE id = ?', (int(id_buscar),))
            productos = cursor.fetchall()

        elif opcion == '2':
            nombre_buscar = input(Style.BRIGHT +"Ingresá el nombre del producto: ").strip()         
            #     Ejecutar la consulta para buscar por nombre
            #     Usar UPPER para hacer la búsqueda insensible a mayúsculas/minúsculas
            #     Usar LIKE para permitir coincidencias parciales
            cursor.execute('SELECT * FROM productos WHERE UPPER(nombre) LIKE ?', ('%' + nombre_buscar.upper() + '%',))
            productos = cursor.fetchall()

        elif opcion == '3':
            categoria_buscar = input(Style.BRIGHT + "Ingresá la categoría: ").strip()
            #    Ejecutar la consulta para buscar por categoría
            #    Usar UPPER para hacer la búsqueda insensible a mayúsculas/minúsculas
            #    Usar LIKE para permitir coincidencias parciales
            cursor.execute('SELECT * FROM productos WHERE UPPER(categoria) LIKE ?', ('%' + categoria_buscar.upper() + '%',))
            productos = cursor.fetchall()

        else:
            print(Fore.RED +"Opción inválida.")
            return []
        
    except Exception as e:
        print(Fore.RED + f'Error en la búsqueda: {e}')
        return []

    finally:
        if conn:
            conn.close()

     #    Retorta los productos encontrados de la funcion exportada desde leer_productos
    return mostrar_productos(productos)