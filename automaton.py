from typing import Tuple, Set, Union
class Automaton:
    def __init__(self) -> None:
        self.transition_function: Dict[str, Dict[str, str]] = {}
        self.start_state: Optional[str] = None
        self.end_states: Set[str] = set()
        self.alphabet: Set[str] = set()


def dfa(n: int) -> Tuple[bool, Automaton]:
    automaton = Automaton()
    automaton.start_state = "z"
    automaton.alphabet = {1, 0}
    automaton.end_states = {"q0"}
    
    if n == 1:
        automaton.transition_function = {"z": {"0": "q0", "1": "q0"}}
    elif n != 1:
        automaton.transition_function = {"z": {"0": "q0", "1": "q1"}}
    
    for state in range(n):
        state_name = 'q' + str(state)
        automaton.transition_function[state_name] = {}
        for digit in [0, 1]:
            next_state = (2 * state + digit) % n
            next_state_name = 'q' + str(next_state)
            automaton.transition_function[state_name][str(digit)] = next_state_name
            
    return automaton
  
