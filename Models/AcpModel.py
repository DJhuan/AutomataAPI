from pydantic import BaseModel
from typing import Set, Dict, Tuple

class  Acp(BaseModel):
    states: Set[str]
    input_symbols: Set[str]
    stack_symbols: Set[str]
    transitions: Dict[str, Dict[str, Dict[str, Tuple[str, Tuple[str, ...]]]]]
    initial_state: str
    initial_stack_symbol: str
    final_states: Set[str]
    acceptance_mode: str