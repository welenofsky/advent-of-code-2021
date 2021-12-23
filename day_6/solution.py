def part_1_solution(inputdata):
    return solution(inputdata, 80)


def part_2_solution(inputdata):
    return solution(inputdata, 256)


def solution(inputdata, days):
    fish_counts = parse_input_data(inputdata)

    for i in range(1, days + 1):
        new_counts = fish_counts.copy()
        for j in range(8, -1, -1):
            if j == 8:
                new_counts['8'] = fish_counts['0']
            elif j == 6:
                new_counts['6'] = fish_counts['0'] + fish_counts['7']
            else:
                new_counts[f"{j}"] = fish_counts[f"{j + 1}"]
        fish_counts = new_counts
    return sum([i for i in fish_counts.values()])


def parse_input_data(data_str):
    fish_counter = {
        '0': 0,
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6': 0,
        '7': 0,
        '8': 0,
    }

    fish_counts = data_str.split(',')
    for count in fish_counts:
        fish_counter[count] += 1

    return fish_counter
