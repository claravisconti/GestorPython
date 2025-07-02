import sqlite3

def conectar(db_name='inventario.db'):
    return sqlite3.connect(db_name)

def crear_base():
    conn = sqlite3.connect('inventario.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL,
            categoria TEXT
        )
    ''')

    conn.commit()
    conn.close()

def insertar_productos_si_vacia():
    conn = sqlite3.connect('inventario.db')
    cursor = conn.cursor()

    # Verificar si la tabla ya tiene datos
    cursor.execute('SELECT COUNT(*) FROM productos')
    cantidad = cursor.fetchone()[0]

    if cantidad == 0:
        # Si está vacía, insertar productos
        productos = [
            ("Camiseta", "Camiseta de algodón", 50, 2999.99, "Ropa"),
            ("Pantalón", "Pantalón de jean", 30, 5999.99, "Ropa"),
            ("Zapatillas", "Zapatillas deportivas", 20, 15000.00, "Calzado"),
            ("Mochila", "Mochila escolar grande", 15, 8999.50, "Accesorios"),
            ("Gorra", "Gorra ajustable", 40, 1999.00, "Accesorios")
        ]

        cursor.executemany('''
            INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
            VALUES (?, ?, ?, ?, ?)
        ''', productos)

        conn.commit()
        print("Productos insertados correctamente.")
    else:
        print("La tabla ya tiene datos. No se insertó nada.")

    conn.close()
