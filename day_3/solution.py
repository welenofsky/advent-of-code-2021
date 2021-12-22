def part_1_solution(inputdata):
    list_len = len(inputdata)

    # Contains a count of all 0's in each position of input data
    one_counts = [0 for _ in list(inputdata[0])]

    for line in inputdata:
        line_parts = [int(x) for x in list(line)]
        for i in range(len(line_parts)):
            one_counts[i] += line_parts[i]

    gamma_rate = ''
    epsilon_rate = ''
    for i in range(len(one_counts)):
        if one_counts[i] >= list_len / 2:
            gamma = '1'
            epsilon = '0'
        else:
            gamma = '0'
            epsilon = '1'

        gamma_rate += gamma
        epsilon_rate += epsilon

    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def part_2_solution(inputdata):
    rating_values = {
        'oxygen_generator': '',
        'co2_scrubber': '',
    }

    for needed_rating in rating_values.keys():
        filtered_records = inputdata
        for i in range(len(filtered_records[0])):
            # Most/Least
            if needed_rating == 'oxygen_generator':
                significant_bit = get_most_significant_bit(filtered_records, i)
            else:
                significant_bit = get_least_significant_bit(filtered_records, i)

            # Filter
            filtered_records = [x for x in filtered_records if x[i] == significant_bit]

            if len(filtered_records) == 1 or i == len(filtered_records[0]) - 1:
                rating_values[needed_rating] = filtered_records[0]
                break

    return int(rating_values['co2_scrubber'], 2) * int(rating_values['oxygen_generator'], 2)


def get_most_significant_bit(records, index):
    count = get_count(records, index)
    return str(int(count >= len(records) / 2))


def get_least_significant_bit(records, index):
    count = get_count(records, index)
    return str(int(count < len(records) / 2))


def get_count(records, index):
    count = 0
    for binary_string in records:
        count += int(binary_string[index])
    return count
