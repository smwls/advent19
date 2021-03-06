from fractions import Fraction
from collections import defaultdict

def parse_map(input_data):
    rows = input_data
    coords = []
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            if rows[i][j] == "#":
                coords.append((j, i))
    return coords

def slope(a1, a2):
    if a1 == a2:
        return "same"
    try:
        return Fraction(a1[1] - a2[1], a1[0] - a2[0])
    except ZeroDivisionError:
        if a1[1] >= a2[1]:
            return float('inf') # this is for part 2
        else:
            return float('-inf')

def get_slope_matrix(asts):
    slope_matrix = [[None for i in asts] for j in asts]
    for i in range(len(asts)):
        for j in range(i, len(asts)):
            slp = slope(asts[i], asts[j])
            slope_matrix[i][j] = slp
            slope_matrix[j][i] = slp
    return slope_matrix

def groups_of_values(lst):
    return [[i for i in range(len(lst)) if lst[i] == y] for y in set(lst)]

def find_best_base_location(asts):
    # naive algorithm - i'm sure there's a much more sophisticated method! 
    slope_matrix = get_slope_matrix(asts)
    best_ast = 0
    best_ast_vis = 0
    for i in range(len(asts)):
        ast_vis = 0
        groups = groups_of_values(slope_matrix[i])
        for grp in groups:
            others = [asts[j] for j in grp]
            if asts[i] in others:
                continue
            elif len(grp) == 1 or asts[i] <= min(others) or asts[i] >= max(others):
                ast_vis += 1
            else:
                ast_vis += 2
        if ast_vis > best_ast_vis:
            best_ast = i
            best_ast_vis = ast_vis
    return (asts[best_ast], best_ast_vis)

def vaporise_asteroids(asts, base):
    negatives = [a for a in asts if a < base or (a[0] == base[0] and a[1] > base[1])]
    positives = [a for a in asts if a > base or (a[0] == base[0] and a[1] < base[1])]
    slopes_of_negatives = [slope(a, base) for a in negatives]
    slopes_of_positives = [slope(a, base) for a in positives]
    negative_groups = [[slope, sorted([(x[0], -1*x[1]) for x in negatives if (x, slope) in zip(negatives, slopes_of_negatives)])] for slope in sorted(set(slopes_of_negatives))]
    positive_groups = [[slope, sorted([(x[0], -1*x[1]) for x in positives if (x, slope) in zip(positives, slopes_of_positives)])] for slope in sorted(set(slopes_of_positives))]
    vaporised = []
    # print(groups)
    for group in negative_groups:
        group[1] = [group[1][-1 * i] for i in range(1, len(group[1]) + 1)]
    groups = positive_groups + negative_groups
    while len(vaporised) < len(negatives) + len(positives):
        to_remove = []
        for group in groups:
            try:
                to_vap = group[1].pop(0)
                vaporised.append((to_vap[0], -1*to_vap[1]))
            except IndexError:
                to_remove.append(group)
        for t in to_remove:
            groups.remove(t)
    return vaporised[198:201]

with open('10', 'r') as f:
    input_data = f.read().split('\n')
    parsed_map = parse_map(input_data)
    # print(parsed_map)
    # print(find_best_base_location(parsed_map))
    print(vaporise_asteroids(parsed_map, (14, 17)))

def run_test_2():
#     t = """.#....#####...#..
# ##...##.#####..##
# ##...#...#.#####.
# ..#.....#...###..
# ..#.#.....#....##"""
    t = """.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##
    """
    parsed_map = parse_map(t.split('\n'))
    # (coord, num) = find_best_base_location(parsed_map)
    # print(coord)
    print(vaporise_asteroids(parsed_map, (11,13)))   

# run_test_2()
def run_test():
    t0 = {'map': """#.#.#
.....
#.#.#
.....
#.#.#
""", 'coord': (2,2), 'num': 8}

    t1 = {'map': """.#..#..###
####.###.#
....###.#.
..###.##.#
##.##.#.#.
....###..#
..#.#..#.#
#..#.#.###
.##...##.#
.....#.#..
    """, 'coord': (6, 3), 'num': 41}
    t2 = {'map': """.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##
    """, 'coord': (11,13), 'num': 210}
    t3 = {'map': """#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###.
    """, 'coord': (1, 2), 'num': 35}

    t4 = {'map': """......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####
    """, 'coord': (5, 8),'num': 33}

    tests = [t0, t1, t2, t3, t4]

    for (test, i) in zip(tests, range(len(tests) + 1)):
        parsed_map = parse_map(test['map'].split('\n'))
        (coord, num) = find_best_base_location(parsed_map)
        if coord == test['coord'] and num == test['num']:
            print('test %d passed'  % i)
        else:
            print("""
test %d failed: 
expected coords %s and num %d, 
but got coords %s and num %d""" 
                    % (i, test['coord'], test['num'], coord, num))
