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

class NFAtoDFAConverter:
    def __init__(self, nfa):
        self.nfa = nfa
        self.dfa_states = set()
        self.dfa_transitions = {}
        self.dfa_initial_state = None
        self.dfa_accept_states = set()
        self.epsilon_closure_cache = {}

    def epsilon_closure(self, nfa_states):
        if frozenset(nfa_states) in self.epsilon_closure_cache:
            return self.epsilon_closure_cache[frozenset(nfa_states)]

        closure = set(nfa_states)
        stack = list(nfa_states)

        while stack:
            state = stack.pop()
            if state in self.nfa.transitions and 'ε' in self.nfa.transitions[state]:
                for target_state in self.nfa.transitions[state]['ε']:
                    if target_state not in closure:
                        closure.add(target_state)
                        stack.append(target_state)

        self.epsilon_closure_cache[frozenset(nfa_states)] = closure
        return closure

    def convert(self):
        nfa_initial_closure = self.epsilon_closure({self.nfa.initial_state})
        self.dfa_initial_state = frozenset(nfa_initial_closure)
        self.dfa_states.add(self.dfa_initial_state)

        queue = [self.dfa_initial_state]
        while queue:
            current_state = queue.pop(0)
            for symbol in self.nfa.alphabet:
                nfa_target_states = set()
                for nfa_state in current_state:
                    if nfa_state in self.nfa.transitions and symbol in self.nfa.transitions[nfa_state]:
                        nfa_target_states.update(self.nfa.transitions[nfa_state][symbol])

                if nfa_target_states:
                    epsilon_closure_target = self.epsilon_closure(nfa_target_states)
                    dfa_target_state = frozenset(epsilon_closure_target)
                    if dfa_target_state not in self.dfa_states:
                        self.dfa_states.add(dfa_target_state)
                        queue.append(dfa_target_state)

                    self.dfa_transitions.setdefault(current_state, {})[symbol] = dfa_target_state

            if any(state in self.nfa.accept_states for state in current_state):
                self.dfa_accept_states.add(current_state)

    def display_dfa(self):
        print("DFA States:", self.dfa_states)
        print("DFA Alphabet:", self.nfa.alphabet)
        print("DFA Transitions:")
        for state, transitions in self.dfa_transitions.items():
            for symbol, target_state in transitions.items():
                print(f"{state} --({symbol})--> {target_state}")
        print("DFA Initial State:", self.dfa_initial_state)
        print("DFA Accept States:", self.dfa_accept_states)

# Create the NFA for recognizing "110" substring
nfa = NFA()
nfa_transitions = {
    'q0': {'ε': {'q1'}},
    'q1': {'1': {'q2'}},
    'q2': {'ε': {'q3'}},
}
nfa.transitions.update(nfa_transitions)
nfa.accept_states.add('q3')

# Convert the NFA to a DFA
converter = NFAtoDFAConverter(nfa)
converter.convert()

# Display the resulting DFA
converter.display_dfa()
print("Name :Aryan Singh")
print("Enrolment no: 0901AM211015")
print("Branch: AIML 3RD Year")
