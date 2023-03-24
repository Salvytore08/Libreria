from fastapi import FastAPI
from pydantic import BaseModel

class PerBiblioteca(BaseModel):
    ID:str
    NOMBRE:str
    EDAD:int
    LIBROS:dict
    
class Lib(BaseModel):
    ID_LIB:str
    NOMBRE:str
    FECHA:str
     

    
app = FastAPI(
    title = 'Server',
    version = 'v0.0.5'
)

biblioteca = {}

@app.get('/')
def check():
   return {
       'Título' : 'Biblioteca STEAM ACADEMY',
       'Versión' : 'v 0.0.5'
   }


@app.get('/personas', tags=['GET'])
def todos():
   return biblioteca


@app.get('/personas/{ID}', tags=['GET'])
def uno(ID:str):
    try:
        return biblioteca[ID]
    except ValueError:
        return f'Por favor ingrese un ID correcto'
    except KeyError:
        return f'Por favor ingrese un ID correcto, el ID {ID}, no se encuentra disponible'
    except Exception:
        return f'Error no definido, intente de nuevo'

@app.post('/personas/{ID}/agregar', tags=['POST'])
def uno_mas(request:PerBiblioteca):
    try:
        biblioteca.update({request.ID : request})
        return 'El usuario se ha agregado correctamente'
    except ValueError:
        return 'Valores incorrectos, por favor intente de nuevo'
    except Exception:
        return 'Error no definido, intente de nuevo'


@app.delete('/personas/{ID}/eliminar', tags=['DELETE'])
def uno_menos(ID:str):
    try:
        biblioteca.pop(ID)
        return 'El usuario se ha eliminado correctamente' 
    except KeyError:
        return 'El usuario no se encuentra disponible, intente de nuevo'
    except Exception:
        return 'Error no definido, intente de nuevo'
        

@app.put('/personas/{ID}/cambiar', tags=['PUT'])
def uno_diferente(ID:str, NewNom:str, NewEdad:int):
    try:
        nuevo = {
            'NOMBRE': NewNom,
            'EDAD' : NewEdad,
            'LIBROS' : biblioteca[ID]['LIBROS']
            }
        biblioteca[ID] = nuevo
        return 'Tu usuario se ha cambiado correctamente'  
    except ValueError:
        return 'Los valores no son correctos, intente de nuevo'
    except KeyError:
        return 'El usuario no se encuentra disponible, no se pudo cambiar la información'
    except Exception:
        return 'Error no definido, intente de nuevo'


@app.put('/libros/{ID}/devolverLib', tags=['PUT'])
def devolver_libro(ID:str, IdLib:str):
    try:
        biblioteca[ID]['LIBROS'][IdLib]['ESTADO'] = 'Devuelto'
        return 'El libro se ha devuelto correctamente'
    except ValueError:
        return 'Los valores no son correctos, intente de nuevo'
    except KeyError:
        return 'El usuario no se encuentra disponible, intente de nuevo'
    except Exception:
        return 'Error no definido, intente de nuevo'


@app.post('/libros/{ID}/prestarLib', tags=['POST'])
def prestar_libro(request:Lib, ID:str):
    try:
        biblioteca[ID.LIBROS][request.ID_LIB] = request
        return 'El libro se ha prestado correctamente'
    except ValueError:
        return 'Los valores no son correctos, intente de nuevo'
    except KeyError:
        return 'El usuario que intenta prestar un libro no se encuentra disponible, intente de nuevo'
    except IndexError:
        return 'El usuario que intenta prestar un libro no se encuentra disponible, intente de nuevo'
    except Exception:
        return 'Error no definido, intente de nuevo'