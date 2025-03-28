def read_file_lines(filename):
    """Read lines from a file and return as a set."""
    with open(filename, 'r', encoding='utf-8') as file:
        return set(file.read().splitlines())


def compare_files(file1, file2):
    """
    Compare two text files and return:
    - lines present in both files
    - lines present only in one of the files
    """
    lines1 = read_file_lines(file1)
    lines2 = read_file_lines(file2)

    same_lines = lines1 & lines2
    diff_lines = lines1.symmetric_difference(lines2)

    return same_lines, diff_lines


