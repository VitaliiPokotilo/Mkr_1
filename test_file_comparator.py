import pytest
import os
from file_comparator import read_file_lines, compare_files, write_results


@pytest.fixture
def create_test_files(tmp_path):
    """Fixture to create test files."""
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"

    file1.write_text("line1\nline2\nline3\nline4")
    file2.write_text("line2\nline3\nline5\nline6")

    return file1, file2


def test_read_file_lines(create_test_files):
    """Test reading lines from files."""
    file1, file2 = create_test_files
    lines1 = read_file_lines(file1)
    lines2 = read_file_lines(file2)

    assert lines1 == {"line1", "line2", "line3", "line4"}
    assert lines2 == {"line2", "line3", "line5", "line6"}


@pytest.mark.parametrize("file1_content,file2_content,expected_same,expected_diff", [
    ("a\nb\nc", "a\nd\ne", {"a"}, {"b", "c", "d", "e"}),
    ("1\n2\n3", "4\n5\n6", set(), {"1", "2", "3", "4", "5", "6"}),
    ("same\nlines", "same\nlines", {"same", "lines"}, set()),
])
def test_compare_files_parametrized(tmp_path, file1_content, file2_content, expected_same, expected_diff):
    """Parametrized test for compare_files function."""
    file1 = tmp_path / "f1.txt"
    file2 = tmp_path / "f2.txt"

    file1.write_text(file1_content)
    file2.write_text(file2_content)

    same, diff = compare_files(file1, file2)
    assert same == expected_same
    assert diff == expected_diff


def test_write_results(tmp_path):
    """Test writing results to files."""
    os.chdir(tmp_path)
    same_lines = {"common1", "common2"}
    diff_lines = {"unique1", "unique2"}

    write_results(same_lines, diff_lines)

    assert os.path.exists("same.txt")
    assert os.path.exists("diff.txt")

    with open("same.txt", "r") as f:
        same_content = set(f.read().splitlines())
    with open("diff.txt", "r") as f:
        diff_content = set(f.read().splitlines())

    assert same_content == same_lines
    assert diff_content == diff_lines