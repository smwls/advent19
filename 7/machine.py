class EndOfTape(Exception):
    pass

def exec_code(inputs, tape, init_head):
    head = init_head
    ops = [lambda x, y : x + y, lambda x, y : x * y, id, id]
    input_counter = 0 if init_head == 0 else 1
    try:
        while tape[head] != 99:
            instruction = list(str(tape[head]))
            opcode = int("".join(instruction[-2:]))
            positions = [int(x) for x in instruction[:-2]]
            num_params = [3, 3, 1, 1, 2, 2, 3, 3][opcode - 1]
            if len(positions) < num_params:
                positions = [0] * (num_params - len(positions)) + positions
            if opcode not in [5, 6]:
                positions[0] = 1
            values = []
            for i in range(num_params):
                if positions[-1 - i]:
                    values.append(tape[head + i + 1])
                else:
                    values.append(tape[tape[head + i + 1]])
            if opcode == 3:
                tape[values[0]] = inputs[input_counter]
                input_counter += 1
                head += num_params + 1
            elif opcode == 4:
                return (tape[values[0]], head + num_params + 1)
                # head += num_params + 1
            elif opcode == 5:
                if values[0] != 0:
                    head = values[1]
                else:
                    head += num_params + 1
            elif opcode == 6:
                if values[0] == 0:
                    head = values[1]
                else:
                    head += num_params + 1
            elif opcode == 7:
                if values[0] < values[1]:
                    tape[values[2]] = 1
                else: 
                    tape[values[2]] = 0
                head += num_params + 1
            elif opcode == 8:
                if values[0] == values[1]:
                    tape[values[2]] = 1
                else:
                    tape[values[2]] = 0
                head += num_params + 1
            else:
                result = ops[opcode - 1](values[0], values[1])
                tape[values[2]] = result
                head += num_params + 1
        raise EndOfTape
    except KeyError as e:
        print("invalid head position")
    except EndOfTape:
        raise EndOfTape

# with open('5', 'r') as f:
#     input_data = [int(x) for x in f.read().split(',')]
#     tape = dict()
#     for x in range(len(input_data)):
#         tape[x] = input_data[x]
#     exec_code([5], tape)