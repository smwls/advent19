from collections import defaultdict

def exec_code(inputs, tape, init_head, init_relative_base):
    head = init_head
    input_counter = 0 #if init_head == 0 else 1
    relative_base = init_relative_base
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
                    try:
                        values.append(tape[head + i + 1])
                    except:
                        print(values)
                        print(head)
                        print(i)
                        print(tape[head + i + 1])
                elif positions[-1 - i] == 1:
                    try:
                        values.append(head + i + 1)
                    except:
                        print(values)
                        print(tape[head + i + 1])
                elif positions[-1 - i] == 2:
                    try:
                        values.append(tape[head + i + 1] + relative_base)
                    except:
                        print(values)
                        print(tape[head + i + 1])                        
            if opcode == 1:
                result = tape[values[0]] + tape[values[1]]
                tape[values[2]] = result
            elif opcode == 2:
                result = tape[values[0]] * tape[values[1]]
                tape[values[2]] = result
            elif opcode == 3:
                tape[values[0]] = inputs[input_counter]
                input_counter += 1
            elif opcode == 4:
                head += num_params + 1
                return (tape[values[0]], head, relative_base)
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
        return ("end", 0,0)
    except KeyError as e:
        print("invalid head position")
    