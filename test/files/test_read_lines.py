import unittest
from pathlib import Path
from unittest.mock import patch, mock_open, Mock

from guet.files.read_lines import read_lines


class TestReadLines(unittest.TestCase):

    @patch('guet.files.read_lines.Path')
    def test_returns_lines_from_file(self, mock_Path):
        path: Path = Mock()
        expected = [
            'Line1',
            'Line2'
        ]
        path.read_text.return_value = 'Line1\nLine2'
        result = read_lines(path)
        self.assertEqual(expected, result)

    @patch('guet.files.read_lines.Path')
    def test_strips_newlines_from_the_end_of_lines(self, mock_Path):
        path: Path = Mock()
        path.read_text.return_value = 'Line1\nLine2\n'
        result = read_lines(path)
        self.assertEqual(['Line1', 'Line2'], result)

    @patch('guet.files.read_lines.Path')
    def test_removes_last_empty_line(self, mock_Path):
        path: Path = Mock()
        path.read_text.return_value = 'Line1\nLine2\n'
        result = read_lines(path)
        self.assertEqual(['Line1', 'Line2'], result)

    @patch('guet.files.read_lines.Path')
    def test_if_given_str_path_convert_to_Path(self, mock_Path):
        mock_Path.return_value.read_text.return_value = 'Line1\nLine2'
        result = read_lines('/path/to/file')
        mock_Path.assert_called_with('/path/to/file')
        self.assertEqual(['Line1', 'Line2'], result)
