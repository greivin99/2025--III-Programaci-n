import csv
import struct

STX = 0x02
ETX = 0x03
DELIMITER = '|'

def limpiar_caracteres(texto):
    return texto.replace('–', '-').replace('—', '-').encode('ascii', errors='ignore').decode('ascii')

def fila_a_trama(fila, campos):
    data_str = DELIMITER.join(limpiar_caracteres(str(fila[c])) for c in campos)
    data_bytes = data_str.encode('ascii')
    return bytes([STX]) + struct.pack('>H', len(data_bytes)) + data_bytes + bytes([sum(data_bytes) % 256, ETX])

def csv_a_tramas(path_csv, campos):
    with open(path_csv, encoding='utf-8') as f:
        return [fila_a_trama(row, campos) for row in csv.DictReader(f)]

def guardar_stream_binario(path_csv, campos, output_path):
    with open(output_path, 'wb') as f:
        f.write(b''.join(csv_a_tramas(path_csv, campos)))