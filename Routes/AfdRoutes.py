from fastapi import APIRouter, Response
from Models.AfdModel import Afd
import dbUtil as db
from automata.fa.dfa import DFA
from automata.base.exceptions import AutomatonException

router = APIRouter()

def gerarAFD(afd: Afd):
    afd = afd.model_dump()
    return DFA(states=afd["states"],
                input_symbols=afd["input_symbols"],
                transitions=afd["transitions"],
                initial_state=afd["initial_state"],
                final_states=afd["final_states"])

@router.post("")
async def new_afd(afd: Afd):
    try:
        gerarAFD(afd)
    except AutomatonException as e:
        return Response(content=str(e), status_code=400)
    
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
    
    try:
        maquina = gerarAFD(automato)
    except AutomatonException as e:
        return Response(content=str(e), status_code=400)
    
    diagrama = maquina.show_diagram()
    
    return Response(content=diagrama.draw(format="png"), media_type="image/png")

@router.post("/{id}")
def run_afd(id: int, word: str):
    automato = db.find(id)
    
    if automato == None:
        return {"error": "Autômato não encontrado"}
    
    else:
        try:
            maquina = gerarAFD(automato)
            aceitacao = maquina.accepts_input(word)
            return {"aceitacao": "Aceito" if aceitacao else "Rejeitado"}
        except AutomatonException as e:
            return Response(content=str(e), status_code=400)