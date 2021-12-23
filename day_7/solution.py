def part_1_solution(inputdata):
    return solution(inputdata, 'part_1')


def part_2_solution(inputdata):
    return solution(inputdata, 'part_2')


def solution(inputdata, test_section):
    data = [int(i) for i in inputdata.split(',')]
    lower_limit, upper_limit = min(data), max(data)

    cur_target = lower_limit
    lowest_fuel_needed = -1
    while cur_target < upper_limit:
        fuel_needed = 0
        stopped_early = False
        for i in data:
            fuel_needed += get_fuel_cost(i, cur_target, test_section)
            if lowest_fuel_needed != -1:
                if fuel_needed > lowest_fuel_needed:
                    stopped_early = True
                    break
        if not stopped_early:
            lowest_fuel_needed = fuel_needed
        cur_target += 1

    return lowest_fuel_needed


def get_fuel_cost(subject, target, test_section):
    diff = abs(subject - target)
    if test_section == 'part_1':
        return diff
    else:
        return diff * (diff / 2 + .5)
