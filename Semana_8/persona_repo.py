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