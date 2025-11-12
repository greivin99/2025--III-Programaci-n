import sqlite3
from Producto import Producto

class Producto_Repo:
    def __init__(self):
        self.__conn = sqlite3.connect("productos.db")
        self.__cursor = self.__conn.cursor()
        self.__cursor.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                categoria TEXT NOT NULL,
                precio REAL NOT NULL,
                proveedor TEXT NOT NULL
            )
        """)
        self.__conn.commit()

    def save(self, producto: Producto):
        self.__cursor.execute("""
            INSERT INTO productos (nombre, categoria, precio, proveedor)
            VALUES (?, ?, ?, ?)
        """, (producto.nombre, producto.categoria, producto.precio, producto.proveedor))
        self.__conn.commit()

    def find_all(self):
        self.__cursor.execute("SELECT * FROM productos")
        rows = self.__cursor.fetchall()
        result = []
        for row in rows:
            prod = Producto(row[1], row[2], row[3], row[4])
            prod.set_id(row[0])
            result.append(prod)
        return result

    def find_by_name(self, name_seq):
        self.__cursor.execute("SELECT * FROM productos WHERE nombre LIKE ?", (f"%{name_seq}%",))
        rows = self.__cursor.fetchall()
        result = []
        for row in rows:
            prod = Producto(row[1], row[2], row[3], row[4])
            prod.set_id(row[0])
            result.append(prod)
        return result

    def find_by_price_range(self, min_price, max_price):
        self.__cursor.execute("SELECT * FROM productos WHERE precio BETWEEN ? AND ?", (min_price, max_price))
        rows = self.__cursor.fetchall()
        result = []
        for row in rows:
            prod = Producto(row[1], row[2], row[3], row[4])
            prod.set_id(row[0])
            result.append(prod)
        return result

    def update(self, product_id, nuevo_precio, nuevo_proveedor):
        self.__cursor.execute("""
            UPDATE productos SET precio = ?, proveedor = ? WHERE id = ?
        """, (nuevo_precio, nuevo_proveedor, product_id))
        self.__conn.commit()

    def delete(self, product_id):
        self.__cursor.execute("DELETE FROM productos WHERE id = ?", (product_id,))
        self.__conn.commit()
