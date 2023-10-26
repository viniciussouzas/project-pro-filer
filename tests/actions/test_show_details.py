from pro_filer.actions.main_actions import show_details  # NOQA
from unittest.mock import patch, Mock


context = {"base_path": "/path/to/your/file"}


def test_file_exists(capsys):
  with patch('os.path.exists', Mock(return_value=True)):
    with patch('os.path.getsize', Mock(return_value=1000)):
      with patch('os.path.isdir', Mock(return_value=False)):
        with patch('os.path.splitext',
                   Mock(return_value=("/path/to/your/file", ".txt"))):
          with patch('os.path.getmtime', Mock(return_value=1609459200)):
            show_details(context)

  captured = capsys.readouterr()
  expected = (
    "File name: file\n"
    "File size in bytes: 1000\n"
    "File type: file\n"
    "File extension: .txt\n"
    "Last modified date: 2021-01-01\n"
  )

  assert captured.out == expected


def test_file_does_not_exists(capsys):
    with patch('os.path.exists', Mock(return_value=False)):
        show_details(context)

    captured = capsys.readouterr()
    expected = "File 'file' does not exist\n"
    assert captured.out == expected


def test_file_with_no_extension(capsys):
    with patch('os.path.exists', Mock(return_value=True)):
        with patch('os.path.getsize', Mock(return_value=1000)):
            with patch('os.path.isdir', Mock(return_value=False)):
                with patch('os.path.splitext',
                           Mock(return_value=("/path/to/your/file", ""))):
                    with patch('os.path.getmtime',
                               Mock(return_value=1609459200)):
                        show_details(context)

    captured = capsys.readouterr()
    expected = (
        "File name: file\n"
        "File size in bytes: 1000\n"
        "File type: file\n"
        "File extension: [no extension]\n"
        "Last modified date: 2021-01-01\n"
    )
    assert captured.out == expected
