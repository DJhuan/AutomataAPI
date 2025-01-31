from fastapi import APIRouter
from Models.AfdModel import Afd
import dbUtil as db
from automata.fa.dfa import DFA

router = APIRouter()

@router.post("")
async def new_afd(afd: Afd):
    id = await db.insert(afd)
    return {"id": id}

@router.get("/{id}")
def get_afd(id: int):
    automato = db.find(id)
    if automato == None:
        return {"error": "Autômato não encontrado"}
    return {"maquina" : automato}

@router.post("/{id}")
def run_afd(id: int, word: str):
    automato = db.find(id)
    if automato == None:
        return {"error": "Autômato não encontrado"}
    else:
        a = automato.dict()
        maquina = DFA(states=a["states"],
                    input_symbols=a["input_symbols"],
                    transitions=a["transitions"],
                    initial_state=a["initial_state"],
                    final_states=a["final_states"])
        aceitacao = maquina.accepts_input(word)
        return {"aceitacao": "Aceito" if aceitacao else "Rejeitado"}

@router.delete("/{id}")
def delete_afd(id: int):
    automato = db.find(id)
    if automato == None:
        return {"error": "Autômato não encontrado"}
    else:
        db.delete(id)
        return {"message": "Autômato deletado com sucesso!"}