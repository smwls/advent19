def exec_code(tape):
    head = 0
    ops = [lambda x, y : x + y, lambda x, y : x * y]
    try:
        while tape[head] != 99:
            opcode = tape[head]
            op = ops[opcode - 1]
            result = op(tape[tape[head + 1]], tape[tape[head + 2]])
            tape[tape[head + 3]] = result
            head += 4
    except KeyError as e:
        print("invalid head position")
    return tape[0]

def find_inputs(value, tape):
    test_tape = dict(tape)
    test_inputs = [(i, j) for i in range(0, 100) for j in range(0, 100)]
    for (i, j) in test_inputs:
        test_tape = dict(tape)
        test_tape[1] = i
        test_tape[2] = j
        result = exec_code(test_tape)
        if result == value:
            return 100 * i + j

with open('2', 'r') as f:
    input_data = [int(x) for x in f.read().split(',')]
    tape = dict()
    for x in range(len(input_data)):
        tape[x] = input_data[x]
    result = find_inputs(19690720, tape)
    print(result)