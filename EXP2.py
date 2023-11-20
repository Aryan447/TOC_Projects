# Let's consider a simple Nondeterministic Finite Automaton (NFA) that accepts strings over the alphabet {0,1} which contain the substring 110 in python.

class NFA:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2', 'q3'}
        self.alphabet = {'0', '1'}
        self.transitions = {
            'q0': {'0': {'q0'}, '1': {'q0', 'q1'}},
            'q1': {'0': {'q2'}, '1': {'q0', 'q1'}},
            'q2': {'0': {'q2'}, '1': {'q3'}},
            'q3': {'0': {'q3'}, '1': {'q3'}}
        }
        self.initial_state = 'q0'
        self.accept_states = {'q3'}

    def process_input(self, input_string):
        current_states = {self.initial_state}

        for symbol in input_string:
            next_states = set()
            for state in current_states:
                if symbol in self.transitions[state]:
                    next_states.update(self.transitions[state][symbol])
            current_states = next_states

        return any(state in self.accept_states for state in current_states)

# Example usage and testing:
if __name__ == "__main__":
    nfa = NFA()

    test_strings = ['0110', '10110', '1100', '010110', '001']
    
    for test_string in test_strings:
        if nfa.process_input(test_string):
            print(f"Accepted: '{test_string}' contains the substring '110'.")
        else:
            print(f"Rejected: '{test_string}' does not contain the substring '110'.")

print("Name :Aryan Singh")
print("Enrolment no: 0901AM211015")
print("Branch: AIML 3RD Year")
