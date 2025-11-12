import io_utils
import person_manager

def process(option):
    if option == 1:
        datos_persona = read_person_data()
        person_manager.store(datos_persona)
    elif option == 2:
        print_persons_data(person_manager.get_all_persons())
    elif option == 3:
        nombre_buscar = leer_nombre_a_buscar()
        print_persons_data(person_manager.find_persons_by_name(nombre_buscar))
    elif option == 4:
        dir_buscar = leer_direccion_a_buscar()
        print_persons_data(person_manager.find_persons_by_dir(dir_buscar))    
    else:
        print("opcion invalida.")

def read_person_data():
    data = []
    print("\n--- Ingreso de datos de persona ---")
    data.append(io_utils.read_str("Nombre: "))
    data.append(io_utils.read_str("Primer apellido: "))
    data.append(io_utils.read_str("Segundo apellido: "))
    data.append(io_utils.read_str("Direccion: "))
    data.append(io_utils.read_str("Fecha de nacimiento (YYYY-MM-DD): "))
    return data

def print_persons_data(list_of_data):
    for persona in list_of_data:
        print(persona)
        #print(persona.nombre + ", edad " + str(persona.edad) + ", apodo = " + persona.apodo) 
        #persona.apodo = "python"
        #print(persona.nombre + ", edad " + str(persona.edad) + ", apodo = " + persona.apodo) 

def leer_nombre_a_buscar():
    return io_utils.read_str("que nombre desea buscar? ")

def leer_direccion_a_buscar():
    return io_utils.read_str("que direccion desea buscar? ")    