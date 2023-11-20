# write a program to implement DFA for accepting all the string ending with 10 over an alphabet { 0, 1}

def dfa(string):
    states = {"A", "B", "C"}
    transitions = {
        "A": {"0": "A", "1": "B"},
        "B": {"0": "C", "1": "B"},
        "C": {"0": "A", "1": "B"},
    }
    final_states = {"C"}
    
    current_state = "A"
    for c in string:
        current_state = transitions[current_state][c]
    
    if current_state in final_states:
        return True
    else:
        return False
    
def main():
    string = input("Enter a string: ")
    if dfa(string):
        print("ACCEPTED")
    else:
        print("NOT ACCEPTED")

main()