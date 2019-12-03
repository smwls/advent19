from collections import defaultdict

#this is just to make defaultdict easier to define
class GridSquare():
    # path_lengths = [0,0]
    def __init__(self):
        self.path_lengths = [0,0]
    # def __str__(self):
    #     return str(self.path_lengths)
    # def __repr__(self):
    #     return repr(self.path_lengths)
    
def manhattan(v1, v2):
    return abs(v1[0] - v2[0]) + abs(v1[1] - v2[1])

def min_intersection_distance(intersections):
    closest = float('inf')
    for intersection in intersections:
        dist = manhattan(intersection, (0,0))
        if dist < closest:
            closest = dist
    return closest

def min_intersection_path_length(intersections, grid):
    closest = float('inf')
    for intersection in intersections:
        dist = grid[intersection].path_lengths[0] + grid[intersection].path_lengths[1]
        if dist < closest:
            closest = dist
    return closest

def find_intersections(input_data):
    intersections = []
    grid = defaultdict(GridSquare)
    for wire in [0,1]:
        path_length = 0
        last = (0, 0)
        for i in input_data[wire]:
            offset_coords = [{
                'U': (last[0], last[1] + k),
                'D': (last[0], last[1] - k),
                'L': (last[0] - k, last[1]),
                'R': (last[0] + k, last[1]),
            }[i[0]] for k in range(1, int(i[1:]) + 1)]
            for coord in offset_coords:
                path_length += 1
                if grid[coord].path_lengths[wire] == 0:
                    grid[coord].path_lengths[wire] = path_length
                if grid[coord].path_lengths[0] > 0 and grid[coord].path_lengths[1] > 0:
                    intersections.append(coord)
            last = offset_coords[-1]
    return (intersections, grid)

with open('3', 'r') as f:
    input_data = [x.split(',') for x in f.read().split('\n')]
    (intersections, grid) = find_intersections(input_data)
    print("min intersection distance: %d" % min_intersection_distance(intersections))
    print("min intersection path length: %d" % min_intersection_path_length(intersections, grid))
