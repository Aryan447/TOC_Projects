class TuringMachine:
    def __init__(self, transitions):
        self.transitions = transitions

    def run(self, tape):
        state = 'q0'  # Initial state
        head_position = 0

        while state != 'q_accept' and state != 'q_reject':
            if head_position >= len(tape):
                break  # Stop if the head goes beyond the tape

            current_symbol = tape[head_position]

            if (state, current_symbol) in self.transitions:
                transition = self.transitions[(state, current_symbol)]
                new_state, new_symbol, move_direction = transition

                tape = tape[:head_position] + new_symbol + tape[head_position + 1:]

                if move_direction == 'R':
                    head_position += 1
                elif move_direction == 'L':
                    head_position -= 1

                state = new_state
            else:
                state = 'q_reject'

        if state == 'q_accept':
            return True
        else:
            return False

# Define the Turing Machine transitions to accept palindromes
transitions = {
    ('q0', '0'): ('q0', '0', 'R'),
    ('q0', '1'): ('q0', '1', 'R'),
    ('q0', ' '): ('q_accept', ' ', 'S'),  # Accept when reaching an empty space
    ('q0', '_'): ('q_accept', '_', 'S'),  # Accept when reaching an underscore
    ('q0', 'x'): ('q0', 'x', 'R'),  # Skip 'x' (used for symmetry)
}

# Function to check if a string is a palindrome
def is_palindrome(input_str):
    input_str = '0' + input_str + '0'  # Add delimiters
    tm = TuringMachine(transitions)
    return tm.run(input_str)

# Test the Turing Machine
input_str = input("Enter a string over {0, 1}: ")
if is_palindrome(input_str):
    print("Accepted: It's a palindrome.")
else:
    print("Rejected: It's not a palindrome.")
print("Name :Aryan Singh")
print("Enrolment no: 0901AM211015")
print("Branch: AIML 3RD Year")
