def part_1_solution(inputdata):
    prev = None
    total = 0

    for numberString in inputdata:
        number = numberString.rstrip()
        if len(number) > 0:
            number = int(number)
            if prev is not None and number > prev:
                total += 1
            prev = number

    return total


def part_2_solution(inputdata):
    prev = None
    total = 0
    curindex = 0

    validnumbers = [int(x) for x in inputdata if len(x.strip()) > 0]
    while curindex < len(validnumbers) - 2:
        frame = validnumbers[curindex:curindex + 3]
        framesum = sum(frame)
        if prev is not None and framesum > prev:
            total += 1
        prev = framesum
        curindex += 1

    return total
