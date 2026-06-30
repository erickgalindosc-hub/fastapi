from fastapi import FastAPI

app = FastAPI()

#endpoint
@app.get("/")
def inicio():
    return{"mensaje:" "hola estoy aprendiendo fastapi"}
