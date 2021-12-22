class Cell:
    def __init__(self, number):
        self.number = number
        self.marked = False


class Board:
    def __init__(self, data):
        self.last_marked = 1
        self.data = [[Cell(x) for x in row] for row in data]

    def is_winner(self):
        # Check horizontal
        for row in self.data:
            if all([cell.marked for cell in row]):
                return True

        # check vertical
        for row in [[row[i] for row in self.data] for i in range(len(self.data[0]))]:
            if all([cell.marked for cell in row]):
                return True

        return False

    def get_score(self):
        return sum([int(cell.number) for row in self.data for cell in row if not cell.marked]) * self.last_marked

    def mark_number(self, number):
        for row in self.data:
            for cell in row:
                if cell.number == int(number):
                    cell.marked = True
                    self.last_marked = cell.number
