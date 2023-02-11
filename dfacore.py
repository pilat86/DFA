def dfa(n):
    alphabets = {1, 0}
    start_state = "z"
    accept_states = {"q0"}
    if n == 1:
        transitions = {"z": {'0': "q0", '1': "q0"}}
    elif n != 1:
        transitions = {"z": {'0': "q0", '1': "q1"}}


    for state in range(n):
        state_name = 'q' + str(state)
        transitions[state_name] = {}
        for digit in [0, 1]:
            next_state = (2 * state + digit) % n
            next_state_name = 'q' + str(next_state)
            transitions[state_name][str(digit)] = next_state_name
    return transitions


def is_accepted(binary_number, start_state, accept_states, transitions):
    current_state = start_state
    for digit in binary_number:
        next_state = transitions[current_state][str(digit)]
        current_state = next_state

    return current_state in accept_states

#####
#TEST
#####

dfa = dfa(3)
print(f"\nTransitions: \n{dfa}\n")
binary_number = "11"

if is_accepted(binary_number, "q0", {"q0"}, dfa):
    print(f"Accepted!\n")
else:
    print(f"Not Accepted!\n")



