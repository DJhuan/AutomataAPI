from fastapi import APIRouter, Response
from Models.MtModel import MT
import dbUtil as db
from automata.tm.dtm import DTM
from automata.base.exceptions import AutomatonException

router = APIRouter()

def gerarMT(mt: MT):
    mt = mt.model_dump()
    return DTM(states=mt["states"],
               input_symbols=mt["input_symbols"],
               tape_symbols=mt["tape_symbols"],
               transitions=mt["transitions"],
               initial_state=mt["initial_state"],
               blank_symbol=mt["blank_symbol"],
               final_states=mt["final_states"])

@router.post("")
async def new_mt(mt: MT):
    try:
        gerarMT(mt)
    except AutomatonException as e:
        return Response(content=str(e), status_code=400)
    id = await db.insert(mt)
    return {"id": id}

@router.get("/{id}")
def get_mt(id: int):
    automato = db.find(id)
    if automato == None:
        return {"error": "Autômato não encontrado"}
    return {"maquina" : automato}

@router.post("/{id}")
def run_mt(id: int, word: str):
    mt = db.find(id)
    if mt == None:
        return {"error": "Autômato não encontrado"}
    else:
        try:
            maquina = gerarMT(mt)
            aceitacao = maquina.accepts_input(word)
            return {"aceitacao": "Aceito" if aceitacao else "Rejeitado"}
        except AutomatonException as e:
            return Response(content=str(e), status_code=400)