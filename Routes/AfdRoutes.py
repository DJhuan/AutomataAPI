from fastapi import APIRouter, Response
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

@router.get("/image/{id}")
def get_afd_image(id: int):
    automato = db.find(id)
    if automato == None:
        return {"error": "Autômato não encontrado"}
    
    a = automato.dict()
    maquina = DFA(states=a["states"],
                input_symbols=a["input_symbols"],
                transitions=a["transitions"],
                initial_state=a["initial_state"],
                final_states=a["final_states"])
    diagrama = maquina.show_diagram()
    
    return Response(content=diagrama.draw(format="png"), media_type="image/png")

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