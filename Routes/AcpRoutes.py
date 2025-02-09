from fastapi import APIRouter, Response
from Models.AcpModel import Acp
import dbUtil as db
from automata.pda.dpda import DPDA
from automata.base.exceptions import AutomatonException

router = APIRouter()

def gerarAcp(acp: Acp):
    acp = acp.model_dump()
    return DPDA(states=acp["states"],
         input_symbols=acp["input_symbols"],
         stack_symbols=acp["stack_symbols"],
         transitions=acp["transitions"],
         initial_state=acp["initial_state"],
         initial_stack_symbol=acp["initial_stack_symbol"],
         final_states=acp["final_states"],
         acceptance_mode=acp["acceptance_mode"])

@router.post("")
async def new_acp(acp: Acp):
    try:
        gerarAcp(acp)
    except AutomatonException as e:
        return Response(content=str(e), status_code=400)
    
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
    
    try:
        maquina = gerarAcp(automato)
    except AutomatonException as e:
        return Response(content=str(e), status_code=400)
    diagrama = maquina.show_diagram()
    
    return Response(content=diagrama.draw(format="png"), media_type="image/png")

@router.post("/{id}")
def run_acp (id: int, word: str):
    automato = db.find(id)
    if automato == None:
        return {"error": "Autômato não encontrado"}
    else:
        try:
            maquina = gerarAcp(automato)
            aceitacao = maquina.accepts_input(word)
            return {"aceitacao": "Aceito" if aceitacao else "Rejeitado"}
        except AutomatonException as e:
            return Response(content=str(e), status_code=400)