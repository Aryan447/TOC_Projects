def turing_machine(tape):
    tape_head = 0

    while tape_head < len(tape):
        current_symbol = tape[tape_head]

        if current_symbol == 'a':
            tape[tape_head] = 'X'
            tape_head += 1
            state = 'q1'
        elif current_symbol == 'X':
            tape_head += 1
            state = 'q1'
        elif current_symbol == 'b':
            tape[tape_head] = 'Y'
            tape_head += 1
            state = 'q2'
        elif current_symbol == 'Y':
            tape_head += 1
            state = 'q2'
        elif current_symbol == 'c':
            tape[tape_head] = 'Z'
            tape_head += 1
            state = 'q3'
        elif current_symbol == 'Z':
            tape_head += 1
            state = 'q3'
        elif current_symbol == '$':
            break
        else:
            return False

    if state == 'q3':
        return True
    else:
        return False

if __name__ == '__main__':
    tape = input('Enter the tape string: ')
    result = turing_machine(tape)

    if result:
        print('Accepted')
    else:
        print('Rejected')