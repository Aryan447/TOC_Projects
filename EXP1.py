# write a program to implement DFA for accepting all the string ending with 00 over an alphabet { 0, 1}

class EvenOnesDFA:
    def __init__(self):
        self.states = {'q0', 'q1'}
        self.alphabet = {'0', '1'}
        self.transition = {
            'q0': {'0': 'q0', '1': 'q1'},
            'q1': {'0': 'q1', '1': 'q0'}
        }
        self.initial_state = 'q0'
        self.accept_state = 'q1'
    
    def process_input(self, input_string):
        current_state = self.initial_state
        for symbol in input_string:
            if symbol not in self.alphabet:
                return False  # Reject if the input contains invalid symbols
            current_state = self.transition[current_state][symbol]
        
        return current_state == self.accept_state

# Example usage and testing:
if __name__ == "__main__":
    dfa = EvenOnesDFA()
    
    test_strings = ['110', '1010', '11111', '010101', '001']
    
    for test_string in test_strings:
        if dfa.process_input(test_string):
            print(f"Accepted: '{test_string}' has an even number of '1's.")
        else:
            print(f"Rejected: '{test_string}' does not have an even number of '1's.")

print("Name :Aryan Singh")
print("Enrolment no: 0901AM211015")
print("Branch: AIML 3RD Year")