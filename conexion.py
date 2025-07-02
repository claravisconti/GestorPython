import sqlite3

def conectar(db_name='inventario.db'):
    return sqlite3.connect(db_name)