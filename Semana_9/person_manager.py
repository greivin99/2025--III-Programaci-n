from Persona import Persona
from persona_repo import Persona_Repo

my_repo = Persona_Repo()

def store(data):
    nueva_persona = Persona(data[0], data[1], data[2], data[3], data[4])
    my_repo.save(nueva_persona)

def get_all_persons():
    return my_repo.find_all()

def find_persons_by_name(name_sequence):
    # esta es la opcion mala!!!
    #personas = my_repo.find_all()
    #result = []
    #for persona in personas:
    #    if persona.nombre.find(name_sequence) != -1:
    #        result.append(persona)
    #return result
    # la opcion correcta
    return my_repo.find_all_by_name(name_sequence)
    

def find_persons_by_dir(dir_sequence):
    return my_repo.find_all_by_dir(dir_sequence)
    #result = []
    #for persona in personas:
    #    if persona.direccion.find(dir_sequence) != -1:
    #        result.append(persona)
    #return result    