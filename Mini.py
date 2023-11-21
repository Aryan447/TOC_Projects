def turing_machine(tape):
    tape = list(tape)  # Convert the input string to a list of characters
    tape_head = 0
    state = 'q0'

    while True:
        current_symbol = tape[tape_head]

        if state == 'q0':
            if current_symbol == 'a':
                tape[tape_head] = 'X'
                tape_head += 1
            elif current_symbol == 'b':
                tape[tape_head] = 'Y'
                tape_head += 1
                state = 'q1'
            elif current_symbol == '$':
                break
            else:
                return False
        elif state == 'q1':
            if current_symbol == 'b':
                tape_head += 1
            elif current_symbol == 'c':
                tape[tape_head] = 'Z'
                tape_head += 1
                state = 'q2'
            else:
                return False
        elif state == 'q2':
            if current_symbol == 'c':
                tape_head += 1
            elif current_symbol == 'X':
                tape[tape_head] = 'a'
                tape_head -= 1
                state = 'q0'
            elif current_symbol == 'Y':
                tape[tape_head] = 'b'
                tape_head -= 1
            elif current_symbol == 'Z':
                tape[tape_head] = 'c'
                tape_head -= 1
            else:
                return False

    return state == 'q0' and tape[tape_head] == '$'

if __name__ == '__main__':
    tape = input('Enter the tape string: ') + '$'
    result = turing_machine(tape)

    if result:
        print('Accepted')
    else:
        print('Rejected')
