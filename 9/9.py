from collections import defaultdict

def exec_code(inputs, tape, init_head):
    head = init_head
    ops = [lambda x, y : x + y, lambda x, y : x * y, id, id]
    input_counter = 0 if init_head == 0 else 1
    relative_base = 0
    try:
        while tape[head] != 99:
            instruction = list(str(tape[head]))
            opcode = int("".join(instruction[-2:]))
            positions = [int(x) for x in instruction[:-2]]
            num_params = [3, 3, 1, 1, 2, 2, 3, 3, 1][opcode - 1]
            if len(positions) < num_params:
                positions = [0] * (num_params - len(positions)) + positions
            values = []
            for i in range(num_params):
                if positions [-1 - i] == 0:
                    values.append(tape[head + i + 1])
                elif positions[-1 - i] == 1:
                    values.append(head + i + 1)
                elif positions[-1 - i] == 2:
                    values.append(tape[head + i + 1] + relative_base)
            if opcode in [1,2]:
                result = ops[opcode - 1](tape[values[0]], tape[values[1]])
                tape[values[2]] = result
            elif opcode == 3:
                tape[values[0]] = inputs[input_counter]
                input_counter += 1
            elif opcode == 4:
                print(tape[values[0]])
            elif opcode == 5:
                if tape[values[0]] != 0:
                    head = tape[values[1]] - num_params - 1
            elif opcode == 6:
                if tape[values[0]] == 0:
                    head = tape[values[1]] - num_params - 1
            elif opcode == 7:
                tape[values[2]] = 1 if tape[values[0]] < tape[values[1]] else 0
            elif opcode == 8:
                tape[values[2]] = 1 if tape[values[0]] == tape[values[1]] else 0
            elif opcode == 9:
                relative_base += tape[values[0]]
            else:
                raise Exception("unrecognised opcode: %s" % opcode)
            head += num_params + 1
    except KeyError as e:
        print("invalid head position")
    finally:
        return "end"

with open('9', 'r') as f:
    input_data = [int(x) for x in f.read().split(',')]
    tape = defaultdict(int)
    for x in range(len(input_data)):
        tape[x] = input_data[x]
    print(exec_code([2], tape, 0))