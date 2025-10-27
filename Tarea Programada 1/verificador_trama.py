import struct

def verificar_tramas(archivo_bin, max_tramas=5):
    with open(archivo_bin, 'rb') as f:
        contenido = f.read()
    
    pos = trama_num = 0
    while pos < len(contenido) and trama_num < max_tramas:
        if contenido[pos] == 0x02:
            etx_pos = contenido.find(b'\x03', pos + 1, pos + 500)
            if etx_pos != -1:
                trama = contenido[pos:etx_pos+1]
                l = struct.unpack('>H', trama[1:3])[0]
                datos = trama[3:3+l].decode('ascii', errors='replace')
                crc = trama[3+l]
                valido = crc == sum(trama[3:3+l]) % 256
                
                print(f"Trama {trama_num+1}: {'Valida' if valido else 'Invalida'}")
                print(f"   Longitud: {l} bytes")
                print(f"   Datos: {datos}")
                print(f"   CRC: 0x{crc:02X} {'' if valido else '(Error)'}")
                print(f"   Tamaño total: {len(trama)} bytes")
                
                trama_num += 1
                pos = etx_pos
        pos += 1

if __name__ == "__main__":
    verificar_tramas("Dhaka_Traffic_Dataset.bin")