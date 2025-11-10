import sqlite3
from Persona import Persona

class Persona_Repo:

    def __init__(self):
        self.__conn = sqlite3.connect("personas.db")
        self.__cursor = self.__conn.cursor()
        self.__cursor.execute("""CREATE TABLE IF NOT EXISTS personas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL, 
            apellido1 TEXT NOT NULL,
            apellido2 TEXT,
            direccion TEXT, 
            fecha TEXT, 
            apodo TEXT
        )""")
        self.__conn.commit()

    def save(self, persona: Persona):
        self.__cursor.execute(f"""INSERT INTO PERSONAS 
        (nombre,apellido1,apellido2,direccion,fecha,apodo) values 
        ('{persona.nombre}','{persona.primer_apellido}', 
        '{persona.segundo_apellido}', '{persona.direccion}', 
        '{persona.fecha_nacimiento}', '{persona.apodo}')
        """)
        self.__conn.commit()

    def find_all(self):
        self.__cursor.execute("SELECT * FROM PERSONAS")
        rows = self.__cursor.fetchall()
        result = []
        for row in rows:
            nuevaPersona = Persona(nombre=row[1],
            apellido1=row[2], apellido2=row[3],
            direccion=row[4], fecha_nacimiento=row[5])
            result.append(nuevaPersona) 
        return result
    
    def find_all_by_name(self, name_seq):
        self.__cursor.execute(f"SELECT * FROM PERSONAS WHERE nombre like '%{name_seq}%'")
        rows = self.__cursor.fetchall()
        result = []
        for row in rows:
            nuevaPersona = Persona(nombre=row[1],
            apellido1=row[2], apellido2=row[3],
            direccion=row[4], fecha_nacimiento=row[5])
            result.append(nuevaPersona) 
        return result
        