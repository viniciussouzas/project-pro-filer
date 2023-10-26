from pro_filer.actions.main_actions import find_duplicate_files  # NOQA
from unittest.mock import patch
import pytest


def test_is_empty():
  context = {"all_files": []}

  assert find_duplicate_files(context) == []


def test_not_duplicates(tmp_path):
    file1 = tmp_path / "test_file1.txt"
    file2 = tmp_path / "test_file2.txt"
    file1.write_text("test file 1")
    file2.write_text("test file 2")

    context = {"all_files": [str(file1), str(file2)]}

    assert find_duplicate_files(context) == []


def test_duplicates(tmp_path):
    file1 = tmp_path / "test_file1.txt"
    file2 = tmp_path / "test_file2.txt"
    file3 = tmp_path / "test_file3.txt"
    file1.write_text("test file 1")
    file2.write_text("test file 1")
    file3.write_text("test file 2")

    context = {"all_files": [str(file1), str(file2), str(file3)]}

    assert find_duplicate_files(context) == [(str(file1), str(file2))]



def test_not_file():
    context = {"all_files": ["non_existent_file1.txt", "non_existent_file2.txt"]}

    with pytest.raises(ValueError, match="All files must exist"):
            find_duplicate_files(context)