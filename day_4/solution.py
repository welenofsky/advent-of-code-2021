from .game import Board


def part_1_solution(inputdata):
    winning_numbers, boards = parse_game_data(inputdata)

    for number in winning_numbers:
        for board in boards:
            board.mark_number(number)
            if board.is_winner():
                return board.get_score()


def part_2_solution(inputdata):
    winning_numbers, boards = parse_game_data(inputdata)

    winning_boards = []
    for number in winning_numbers:
        for board_index in range(len(boards)):
            if board_index in winning_boards:
                continue

            boards[board_index].mark_number(number)
            if boards[board_index].is_winner():
                winning_boards.append(board_index)

    # get score from last winner tuple data
    return boards[winning_boards.pop()].get_score()


def parse_game_data(data):
    boards = []
    winning_numbers = data[0].split(',')

    # Game data only
    game_data = []
    for row in data[2:]:
        if not row:
            boards.append(Board(game_data))
            game_data = []
        else:
            game_data.append([int(x) for x in row.split()])

    # In case the last line wasn't empty
    if len(game_data):
        boards.append(Board(game_data))

    return [winning_numbers, boards]
