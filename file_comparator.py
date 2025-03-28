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


def write_results(same_lines, diff_lines):
    """Write comparison results to output files."""
    with open('same.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(sorted(same_lines)))

    with open('diff.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(sorted(diff_lines)))



def main(file1, file2):
    """Main function to compare two files and write results."""
    same_lines, diff_lines = compare_files(file1, file2)
    write_results(same_lines, diff_lines)
    print(f"Comparison completed. Results written to same.txt and diff.txt")