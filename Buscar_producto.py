from conexion import conectar
from leer_productos import leer_productos

#     SOLICITAR DATOS DEL PRODUCTO A BUSCAR
def buscar_productos():
    print("\nOpciones de búsqueda:")
    print("1. Buscar por ID")
    print("2. Buscar por Nombre")
    print("3. Buscar por Categoría")
    opcion = input("Elegí una opción: ")

    productos = []

    try:
        conn = conectar()
        cursor = conn.cursor()

        if opcion == '1':
            id_buscar = input("Ingresá el ID del producto: ").strip()
            if not id_buscar.isdigit():
                print("El ID debe ser un número entero.")
                return []

            cursor.execute('SELECT * FROM productos WHERE id = ?', (int(id_buscar),))
            productos = cursor.fetchall()

        elif opcion == '2':
            nombre_buscar = input("Ingresá el nombre del producto: ").strip()
            cursor.execute('SELECT * FROM productos WHERE UPPER(nombre) LIKE ?', ('%' + nombre_buscar.upper() + '%',))
            productos = cursor.fetchall()

        elif opcion == '3':
            categoria_buscar = input("Ingresá la categoría: ").strip()
            cursor.execute('SELECT * FROM productos WHERE UPPER(categoria) LIKE ?', ('%' + categoria_buscar.upper() + '%',))
            productos = cursor.fetchall()

        else:
            print("Opción inválida.")
            return []
        
    except Exception as e:
        print(f'Error en la búsqueda: {e}')
        return []

    finally:
        if conn:
            conn.close()

    return leer_productos()