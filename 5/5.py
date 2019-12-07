def exec_code(inpt, tape):
    head = 0
    ops = [lambda x, y : x + y, lambda x, y : x * y, id, id]
    try:
        while tape[head] != 99:
            instruction = list(str(tape[head]))
            opcode = int("".join(instruction[-2:]))
            print(opcode)
            positions = [int(x) for x in instruction[:-2]]
            num_params = [3, 3, 1, 1, 2, 2, 3, 3][opcode - 1]
            if len(positions) < num_params:
                positions = [0] * (num_params - len(positions)) + positions
            print("positions are %s " % str(positions))
            if opcode not in [5, 6]:
                positions[0] = 1
            values = []
            for i in range(num_params):
                if positions[-1 - i]:
                    values.append(tape[head + i + 1])
                else:
                    values.append(tape[tape[head + i + 1]])
            # values = [(positions[-1 - i] * ) + (1 - positions[-1 - i]) * tape[tape[head + i + 1]] for i in range(num_params)]
            print("values are %s" % str(values))
            if opcode == 3:
                print("store input %d at position %d" % (inpt, values[0]))
                tape[values[0]] = inpt
                head += num_params + 1
            elif opcode == 4:
                print('output %d' % values[0])
                print(tape[values[0]])
                head += num_params + 1
            elif opcode == 5:
                if values[0] != 0:
                    print("jumping to %d because %d is true" % (values[1], values[0]))
                    head = values[1]
                else:
                    head += num_params + 1
            elif opcode == 6:
                if values[0] == 0:
                    print("jumping to %d because %d is false" % (values[1], values[0]))                    
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
                print("perform operation %d with %d and %d and store at position %d" % (opcode, values[0], values[1], values[2]))
                result = ops[opcode - 1](values[0], values[1])
                tape[values[2]] = result
                head += num_params + 1
            # if opcode == 3:
            #     tape[tape[head + 2]] = tape[tape[head + 1]]
            #     head += 3
            # op = ops[opcode - 1]
            # result = op(tape[tape[head + 1]], tape[tape[head + 2]])
            # tape[tape[head + 3]] = result
            # head += 4
    except KeyError as e:
        print("invalid head position")
    # return tape[0]

with open('5', 'r') as f:
    input_data = [int(x) for x in f.read().split(',')]
    tape = dict()
    for x in range(len(input_data)):
        tape[x] = input_data[x]
    exec_code(5, tape)