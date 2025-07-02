
from conexion import conectar
from colorama import init, Fore, Style

#     MOSTRAR TODOS LOS PRODUCTOS

def leer_productos():
    #    Inicializar conn como None para manejar el cierre de conexión en el bloque finally
    conn = None
    #     TRY-EXCEPT-FINALLY: Intentar conectar a la base de datos y realizar la búsqued, mostrar errores y ejecutar el cierre de la conexión
    #     Usar un bloque try-except para manejar errores de conexión o consulta
    try:
        conn = conectar()
        cursor = conn.cursor()

    #     Ejecutar la consulta para leer todos los productos
        cursor.execute('SELECT * FROM productos')
        productos = cursor.fetchall()

    #     Si no se encontraron productos, imprimir un mensaje y retornar una lista vacía
        if not productos:
            print(Fore.RED + "\nNo se encontraron productos.")
            return
        
        print("\n" + "-" * 90)
        print(f"{'ID':<5} {'Nombre':<20} {'Descripción':<25} {'Cant.':<8} {'Precio':<10} {'Categoría':<15}")
        print("-" * 90)
    #     Si se encontraron productos, imprimirlos en un formato legible
        for producto in productos: 
            # print(f"ID: {producto[0]}, Nombre: {producto[1]}, Descripción: {producto[2]}, Cantidad: {producto[3]}, Precio: {producto[4]}, Categoría: {producto[5]}")
            print(f"{producto[0]:<5} {producto[1]:<20} {producto[2]:<25} {producto[3]:<8} {producto[4]:<10} {producto[5]:<15}")
            print("-" * 90)

        return productos
    
    #     Manejar errores de conexión o consulta
    except Exception as e:
        print(Fore.RED + f"Error al leer productos: {e}")
        return []

    #     Asegurarse de cerrar la conexión a la base de datos
    finally:
        if 'conn' in locals():
            conn.close()


#     MOSTRAR PRODUCTOS ESPECIFICOS

def mostrar_productos(productos):
     #     Si no se encontraron productos, imprimir un mensaje y retornar una lista vacía
    if not productos:
        print(Fore.RED +"\nNo se encontraron productos.")
        return

    #     Si se encontraron productos, imprimirlos en un formato legible
    print(Style.BRIGHT + "\nResultados encontrados:")
    print("\n" + "-" * 90)
    print(f"{'ID':<5} {'Nombre':<20} {'Descripción':<25} {'Cant.':<8} {'Precio':<10} {'Categoría':<15}")
    print("-" * 90)
    #     Si se encontraron productos, imprimirlos en un formato legible
    for producto in productos: 
        # print(f"ID: {producto[0]}, Nombre: {producto[1]}, Descripción: {producto[2]}, Cantidad: {producto[3]}, Precio: {producto[4]}, Categoría: {producto[5]}")
        print(f"{producto[0]:<5} {producto[1]:<20} {producto[2]:<25} {producto[3]:<8} {producto[4]:<10} {producto[5]:<15}")
        print("-" * 90)