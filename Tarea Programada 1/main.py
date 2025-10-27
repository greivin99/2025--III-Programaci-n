import xml_module
import json_module
from trama_module import guardar_stream_binario
import csv
import os

def main():
    csv_path = "Tarea Programada I\Dhaka_Traffic_Dataset.csv"
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            columnas = next(reader)
            filas = [next(reader) for _ in range(5)]
        
        print("\n=== Columnas y primeras 5 filas ===")
        for i, col in enumerate(columnas, 1):
            print(f"{i}: {col}")
        print("\nPrimeras filas:")
        for i, fila in enumerate(filas, 1):
            print(f"Fila {i}: {fila}")
        
        print("\nFormatos disponibles:")
        print("1: XML")
        print("2: JSON") 
        print("3: TRAMA")
        opcion = input("\nFormato al que desea transformar → (1-3): ").strip()
        
        seleccion = input("Numero de columnas a usar (ej: 1,3,5): ").strip()
        campos = [columnas[int(x)-1] for x in seleccion.split(',')]
        
        print(f"\n Transformando solo las siguientes columnas: {', '.join(campos)}")
        
        nombre_base = os.path.splitext(os.path.basename(csv_path))[0]
        
        if opcion == "1":
            xml_module.csv_to_xml(csv_path, f"{nombre_base}.xml", campos)
            print(f"XML generado: {nombre_base}.xml")
        elif opcion == "2":
            json_module.csv_to_json(csv_path, f"{nombre_base}.json", campos)
            print(f"JSON generado: {nombre_base}.json")
        elif opcion == "3":
            guardar_stream_binario(csv_path, campos, f"{nombre_base}.bin")
            print(f"Tramas generadas: {nombre_base}.bin")
        else:
            print("Opcion invalida")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()