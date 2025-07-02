from conexion import conectar
from leer_productos import mostrar_productos

def mostrar_reporte():
    #     Lista para almacenar los productos encontrados
    productos = []
    #    Inicializar conn como None para manejar el cierre de conexión en el bloque finally
    conn = None
    #     TRY-EXCEPT-FINALLY: Intentar conectar a la base de datos y realizar la búsqued, mostrar errores y ejecutar el cierre de la conexión
    #     Usar un bloque try-except para manejar errores de conexión o consulta
    try:
        conn = conectar()
        cursor = conn.cursor()

        #   Solicitar al usuario que ingrese la cantidad máxima límite
        while True:
            entrada = input("Ingresá la cantidad máxima límite: ").strip()
            if entrada.isdigit():
                cantidad_buscar = int(entrada)
                break  # Solo se rompe si la entrada es válida
            print("Por favor, ingresá un número entero válido.")

        #   Realizar la consulta para buscar productos con cantidad menor o igual al límite especificado
        cursor.execute('SELECT * FROM productos WHERE cantidad <= ?', (cantidad_buscar,))
        productos = cursor.fetchall()
        
        #   Verificar si se encontraron productos
        if not productos:
            print("\nNo se encontraron productos con límite.")
            return []

        #   Mostrar los detalles del producto encontrado
        mostrar_productos(productos)

    except Exception as e:
        print(f'\nError en la búsqueda: {e}')
        return []

    finally:
        if conn:
            conn.close()