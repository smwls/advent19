from collections import defaultdict
from machine import exec_code

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Robot():
    def __init__(self):
        self.position = Point(0,0)
        self.direction = "U"

    def turn(self, direct):
        self.direction = ["U", "L", "D", "R"][({"U": 0, "L":1, "D":2, "R":3}[self.direction] - 2*direct + 1 ) % 4]

    def step(self):
        if self.direction == "U":
            self.position.y += 1
        elif self.direction == "D":
            self.position.y -= 1
        elif self.direction == "L":
            self.position.x -= 1
        elif self.direction == "R":
            self.position.x += 1
        else:
            raise Exception("unknown direction")

    def coords(self):
        return (self.position.x, self.position.y)

def render(panel_state):
    xs = [x[0] for x in panel_state.keys() if panel_state[x] == 0]
    ys = [x[1] for x in panel_state.keys() if panel_state[x] == 0]
    # height = max(ys) - min(ys)
    # width = max(xs) - min(xs)
    # print(panel_state)
    # print(height)
    # print(width)
    image = ""
    for row in range(max(ys), min(ys) - 1, -1):
        for col in range(min(xs), max(xs)):
            if panel_state[(col, row)] == 0:
                image += " "
            else:
                image += "#"
        image += '\n' 
    return image

with open('11', 'r') as f:
    input_data = [int(x) for x in f.read().split(',')]
    tape = defaultdict(int)
    for x in range(len(input_data)):
        tape[x] = input_data[x]
    panel_state = defaultdict(int)
    robot = Robot()
    code_input = 1
    paint_output = 0
    turn_output = 0
    head = 0
    relative_base = 0
    painted = defaultdict(int)
    while paint_output != "end" or turn_output != "end":
        (paint_output, head, relative_base) = exec_code([code_input], tape, head, relative_base)
        if paint_output == "end":
            break
        (turn_output, head, relative_base) = exec_code([code_input], tape, head, relative_base)
        panel_state[robot.coords()] = paint_output
        if not painted[robot.coords()]:
            painted[robot.coords()] += 1
        robot.turn(turn_output)
        robot.step()
        code_input = panel_state[robot.coords()]
    print(render(panel_state))
    # print(len([x for x in painted.keys() if painted[x] > 0]))