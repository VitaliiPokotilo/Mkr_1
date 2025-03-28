def read_file_lines(filename):
    """Read lines from a file and return as a set."""
    with open(filename, 'r', encoding='utf-8') as file:
        return set(file.read().splitlines())





