from itertools import permutations
from machine import exec_code, EndOfTape

class Amp():
    def __init__(self, head, tape):
        self.head = head
        self.tape = tape
        self.done = False
        self.output = 0

    def run(self, phase, amp_input):
        try:
            (output, head) = exec_code([phase, amp_input], self.tape, self.head)
            self.head = head
            self.output = output
            return output
        except EndOfTape:
            self.done = True
            return self.output

    def __repr__(self):
        return "head position: %d\ndone: %s\noutput: %s\n\n" % (self.head, self.done, self.output)

    def __str__(self):
        return "head position: %d\ndone: %s\noutput: %s\n\n" % (self.head, self.done, self.output)

def run_amps(tape):
    outputs = []
    for perm in permutations(range(5, 10)):
        amplifiers = []
        for i in range(5):
            amp = Amp(0, dict(tape))
            amplifiers.append(amp)
        signal = 0
        amp = 0
        while not all(map(lambda a : a.done, amplifiers)):
            signal = amplifiers[amp].run(perm[amp], signal)
            amp = (amp + 1) % 5
        print(amplifiers)
        outputs.append(signal)
    print(outputs)
    return(max(outputs))

with open('7', 'r') as f:
    input_data = [int(x) for x in f.read().split(',')]
    tape = dict()
    for x in range(len(input_data)):
        tape[x] = input_data[x]
    print(run_amps(tape))