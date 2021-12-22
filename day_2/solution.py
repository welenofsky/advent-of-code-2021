def part_1_solution(inputdata):
    horizontal = 0
    depth = 0
    for op in inputdata:
        direction, distance = op.split()
        if direction == 'forward':
            horizontal += int(distance)
        elif direction == 'down':
            depth += int(distance)
        elif direction == 'up':
            depth -= int(distance)
        else:
            print(f"Error, unknown direction: {direction}")

    return depth * horizontal


def part_2_solution(inputdata):
    horizontal = 0
    depth = 0
    aim = 0

    for op in inputdata:
        direction, distance = op.split()
        distance = int(distance)
        if direction == 'forward':
            horizontal += distance
            depth += (aim * distance)
        elif direction == 'down':
            aim += distance
        elif direction == 'up':
            aim -= distance
        else:
            print(f"Error, unknown direction: {direction}")

    return depth * horizontal

