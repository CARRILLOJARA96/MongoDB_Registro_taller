import os
import pprint

def clear_system(function):
    
    def wrap(*args, **kwargs):
        os.system('cls')
        result = function(*args, **kwargs)
        input('Presiona Enter para continuar...')
        os.system('cls')
        return result
    
    wrap.__doc__=function.__doc__
    return wrap

def show_user(user):
    pp=pprint.PrettyPrinter(indent=4)
    pp.pprint(user)

@clear_system
def create_user(collection):
    """A) Crear un usuario"""

    username=input('Username: ')
    edad=int(input('Edad: '))
    email=input('Email: ')

    #Documento -> Json -> Dic
    user=dict(username=username, edad=edad, email=email)

    direccion = input ('Desea ingresar su direccion? (S/N)').lower()

    if direccion == 's':
        user ['direccion'] = get_address()

    collection.insert_one(user)
    show_user(user)
    return user

def get_address():
    calle=input('Calle: ')
    ciudad = input ('Ciudad: ')
    estado = input ( 'Estado: ')
    codigo_postal = input ('Codigo postal: ')

    direccion = dict(calle=calle,
                     ciudad=ciudad,
                     estado=estado,
                     codigo_postal=codigo_postal)

    return direccion
@clear_system
def get_user(collection):
    """B) Consultar usuario"""
    username = input ('Username: ')

    user = collection.find_one(
        {'username':username},
        {'_id':False}
    )

    if user:
        show_user(user)
        return user
    else:
        print('No fue posible obtener documento alguno')

def delete_user(collection):
    """C) Eliminar usuario"""
    username = input('Username: ')

    return collection.delete_one(
            {'username':username}

    )

def update_user():
    """D) Actualizar usuario"""
    print('Actualizar usuario')    

def default(*args, **kwargs):
    print('Opcion no valida')

#PENDIENTE
#CREAR LA FUNCION ACTUALIZAR(UPDATE)
#CREAR UNA FUNCION DE DECRECER SI SE ELIMINA ALGÚN REGISTRO EN ATLAS