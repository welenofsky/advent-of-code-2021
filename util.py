def retrieve_input_data(filename='input.txt'):
    with open(filename, 'r') as f:
        data = f.read().splitlines()
        if len(data) == 1:
            return data[0]
        return data
