def retrieve_input_data(filename='input.txt'):
    with open(filename, 'r') as f:
        return f.read().splitlines()
