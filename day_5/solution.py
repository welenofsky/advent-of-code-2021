def part_1_solution(inputdata):
    plane = {}
    for line_coords in inputdata:
        line = get_simple_line(parse_line_data(line_coords))
        for str_point in line:
            if str_point in plane:
                plane[str_point] += 1
            else:
                plane[str_point] = 1

    return len([x for x in plane.values() if x >= 2])


def part_2_solution(inputdata):
    plane = {}
    for line_coords in inputdata:
        line = get_complex_line(parse_line_data(line_coords))
        for str_point in line:
            if str_point in plane:
                plane[str_point] += 1
            else:
                plane[str_point] = 1

    return len([x for x in plane.values() if x >= 2])


def parse_line_data(line):
    return [[int(n) for n in x.strip().split(',')] for x in line.split('->')]


def get_simple_line(coords):
    coords.sort()
    (x1, y1), (x2, y2) = coords

    # For now only simple horizontal/vertical lines
    if x1 != x2 and y1 != y2:
        return []

    # Part 1 assumption is that x1,x2 or y1,y2 will be same val
    if x1 == x2:
        line = [f"{x1},{i}" for i in range(y1, y2+1)]
    else:
        line = [f"{i},{y1}" for i in range(x1, x2+1)]
    return line


def get_complex_line(coords):
    (x1, y1), (x2, y2) = coords
    line_coords = [f"{x1},{y1}"]
    new_coords = coords
    final_point = f"{x2},{y2}"
    while final_point not in line_coords:
        (new_x, new_y) = get_next_number(new_coords)
        line_coords.append(f"{new_x},{new_y}")
        new_coords = [(new_x, new_y), (x2, y2)]
    return line_coords


def get_next_number(coords):
    (x1, y1), (x2, y2) = coords
    new_x = int(x2)
    new_y = int(y2)

    # transition from x1,y1 -> x2,y2
    if x1 > x2:
        new_x = int(x1) - 1
    elif x1 < x2:
        new_x = int(x1) + 1

    if y1 > y2:
        new_y = int(y1) - 1
    elif y1 < y2:
        new_y = int(y1) + 1

    # new x1,y1
    return [new_x, new_y]
