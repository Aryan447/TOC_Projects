class State:
    def __init__(self, is_accepting):
        self.id = None
        self.is_accepting = is_accepting
        self.transitions = []

next_state_id = 0
states = []  # Store states in a list

def create_state(is_accepting):
    global next_state_id
    state = State(is_accepting)
    state.id = next_state_id
    next_state_id += 1
    states.append(state)  # Add state to the list
    return state

def add_transition(state, c, next_state):
    state.transitions.append((c, next_state))

def convert_regular_expression_to_nfa(regex):
    global next_state_id
    next_state_id = 0

    # Create the start state.
    start_state = create_state(False)

    i = 0
    while i < len(regex):
        if regex[i] != '*' and regex[i] != '|':
            # If the character is a literal, create a new state and add a transition.
            next_state = create_state(False)
            add_transition(start_state, regex[i], next_state.id)
            start_state = next_state
        elif regex[i] == '*':
            # If the character is a star, create a new state and add self-loop and transition.
            next_state = create_state(False)
            add_transition(start_state, regex[i], start_state.id)
            add_transition(start_state, regex[i], next_state.id)
            start_state = next_state
        elif regex[i] == '|':
            # If the character is a |, create two new states and add transitions.
            next_state_1 = create_state(False)
            next_state_2 = create_state(False)
            add_transition(start_state, regex[i], next_state_1.id)
            add_transition(start_state, regex[i], next_state_2.id)
            start_state = next_state_1
        i += 1

    # The final state is the current state.
    start_state.is_accepting = True

    return start_state

def print_nfa(nfa):
    for state in states:  # Iterate through the list of states
        print(f"State {state.id}: {'accepting' if state.is_accepting else 'not accepting'}")
        for transition in state.transitions:
            print(f"  {transition[0]} -> {transition[1]}")

if __name__ == "__main__":
    regex = "a*|b"
    nfa = convert_regular_expression_to_nfa(regex)

    # Print the NFA.
    print_nfa(nfa)
