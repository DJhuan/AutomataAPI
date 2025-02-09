from fastapi import FastAPI
from Routes.AfdRoutes import router as afd_router
from Routes.AcpRoutes import router as acp_router
import dbUtil as db

app = FastAPI()
app.include_router(afd_router, prefix="/afd")
app.include_router(acp_router, prefix="/acp")

@app.get("/")
def read_root():
    greetings = """Olá, saudações da AutomataAPI!
    Para criar um automato/MT é só seguir a rota:
    /<tipo>
    Em que tipo pode ser
    afd: autômato finito determinístico
    acp: autômato com pilha
    mt:  máquina de turing
    
    Para maiores informações consulte o manual da API!
    """
    return {"greetings": greetings}

@app.delete("/{id}")
def delete_machine(id: int):
    mensagem = db.delete(id)
    return {"message": mensagem}