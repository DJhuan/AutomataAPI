from pydantic import BaseModel
from typing import Set, Dict

class  Afd(BaseModel):
    states: Set[str]
    input_symbols: Set[str]
    transitions: Dict[str, Dict[str, str]]
    initial_state: str
    final_states: Set[str]