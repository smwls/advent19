from collections import defaultdict

def count_orbits(orbit_map):
    to_visit = list(orbit_map.keys())
    count = 0
    while len(to_visit) > 0:
        next_orb = to_visit.pop()
        count += len(orbit_map[next_orb])
        to_visit += orbit_map[next_orb]
    return count

def parse_orbit_map(input_data):
    orbit_map = defaultdict(list)
    for orb in input_data:
        (ctr, sat) = orb.split(')')
        orbit_map[ctr].append(sat)
    return orbit_map

def parse_reverse_orbit_map(input_data):
    reverse_orbit_map = defaultdict(list)
    for orb in input_data:
        (ctr, sat) = orb.split(')')
        reverse_orbit_map[sat] = ctr
    return reverse_orbit_map

def find_path_to_com(reverse_orbit_map, start):
    path = []
    current = start
    while current != "COM":
        path.append(current)
        current = reverse_orbit_map[current]
    return path

def compare_orbit_paths(reverse_orbit_map, p1, p2):
    p1_path = find_path_to_com(reverse_orbit_map, p1)
    p2_path = find_path_to_com(reverse_orbit_map, p2)
    shorter = p1_path if len(p1_path) <= len(p2_path) else p2_path
    longer = p2_path if len(p1_path) <= len(p2_path) else p1_path
    ll = len(longer)
    ls = len(shorter)
    count = ll - ls
    for i in range(1, len(shorter)):
        if shorter[i] != longer[i + ll - ls]:
            count += 2
        else:
            return count

with open('6', 'r') as f:
    input_data = f.read().split('\n')
    orbit_map = parse_orbit_map(input_data)
    reverse_orbit_map = parse_reverse_orbit_map(input_data)
    print(count_orbits(orbit_map))
    print(compare_orbit_paths(reverse_orbit_map, "SAN", "YOU"))