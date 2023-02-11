from typing import Tuple, Set, Union
class Automaton:
    def __init__(self) -> None:
        self.transition_function: Dict[str, Dict[str, str]] = {}
        self.start_state: Optional[str] = None
        self.end_states: Set[str] = set()
        self.alphabet: Set[str] = set()

def dfa(n: int) -> Tuple[bool, Automaton]:
    automaton = Automaton()
    automaton.alphabet = {1, 0}
    automaton.start_state = "q0"
    automaton.end_states = {"q0"}
    

    for state in range(n):
        state_name = 'q' + str(state)
        automaton.transition_function[state_name] = {}
        for digit in automaton.alphabet:
            next_state = (2 * state + digit) % n
            next_state_name = 'q' + str(next_state)
            automaton.transition_function[state_name][digit] = next_state_name
    return automaton.transition_function


def is_accepted(binary_number, start_state, accept_states, transitions):
    current_state = start_state
    for digit in binary_number:
        next_state = transitions[current_state][int(digit)]
        current_state = next_state

    return current_state in accept_states

dfa = dfa(3)
print(f"\nTransitions: \n{dfa}\n")
binary_number = "11"

if is_accepted(binary_number, "q0", {"q0"}, dfa):
    print(f"Accepted!\n")
else:
    print(f"Not Accepted!\n")