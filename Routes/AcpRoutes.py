from fastapi import APIRouter, Response
from Models.AcpModel import Acp
import dbUtil as db
from automata.pda.dpda import DPDA

router = APIRouter()

@router.post("")
async def new_acp(acp: Acp):
    id = await db.insert(acp)
    return {"id": id}

@router.get("/{id}")
def get_acp(id: int):
    automato = db.find(id)
    if automato == None:
        return {"error": "Autômato não encontrado"}
    return {"maquina" : automato}

@router.get("/image/{id}")
def get_acp_image(id: int):
    automato = db.find(id)
    if automato == None:
        return {"error": "Autômato não encontrado"}
    
    a = automato.dict()
    maquina = DPDA(states=a["states"],
                   input_symbols=a["input_symbols"],
                   stack_symbols=a["stack_symbols"],
                   transitions=a["transitions"],
                   initial_state=a["initial_state"],
                   initial_stack_symbol=a["initial_stack_symbol"],
                   final_states=a["final_states"],
                   acceptance_mode=a["acceptance_mode"])
    diagrama = maquina.show_diagram()
    
    return Response(content=diagrama.draw(format="png"), media_type="image/png")

@router.post("/{id}")
def run_acp (id: int, word: str):
    automato = db.find(id)
    if automato == None:
        return {"error": "Autômato não encontrado"}
    else:
        a = automato.dict()
        maquina = DPDA(states=a["states"],
                       input_symbols=a["input_symbols"],
                       stack_symbols=a["stack_symbols"],
                       transitions=a["transitions"],
                       initial_state=a["initial_state"],
                       initial_stack_symbol=a["initial_stack_symbol"],
                       final_states=a["final_states"],
                       acceptance_mode=a["acceptance_mode"])
        aceitacao = maquina.accepts_input(word)
        return {"aceitacao": "Aceito" if aceitacao else "Rejeitado"}