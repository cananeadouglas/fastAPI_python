

from fastapi import FastAPI

from rotas import router


app = FastAPI(
    title="Douglas - Teste FastAPI",
    description="test",
    version="0.0.1",
)

@app.get('/')
def get_root():
    return {"mensagem": "Api de valor"}

app.include_router(router, prefix='')

# principais métodos
# GET, POST, HEAD, PUT, PATCH, DELETE, OPTION