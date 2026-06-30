from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

lista_clientes: list[cliente] =[]

class cliente(BaseModel):
    id: int
    nombre: str
    email : str
    descripcion: str



#(id, nombre , email, descripcion)

#endpoint los clientes, obtener
@app.get("/clientes")
def listar_clientes():
    return lista_clientes


#endpoint un solo cliente
@app.get("/cliente/{cliente_id}")
def listar_cliente(cliente_id: int):
    #recorrer a lista clientes
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.get("id")== cliente_id:
            return obj_cliente
        

#endpoint para crear un cliente y agregar a la lista

@app.post("/clientes")
def crear_cliente(datos_cliente: cliente):
    lista_clientes.append(datos_cliente)
    return datos_cliente
   