import unittest
import argparse
import datetime
from .context import terminal


class TestTerminalArguments(unittest.TestCase):

    """ Test terminal arguments """
    def test_terminal_returns_type_of_Argument_Parser(self):
        arguments = terminal.parse_arguments(
            ['-s', '01-01-2022', '-e', '05-01-2022'])
        self.assertIsInstance(arguments, argparse.Namespace)
    
    """ Test terminal arguments """
    def test_terminal_start_date_argument_is_date(self):
        arguments = terminal.parse_arguments(
            ['-s', '01-01-2022', '-e', '05-01-2022'])
        self.assertIsInstance(arguments.start_date, datetime.date)

    """ Test terminal arguments """
    def test_terminal_end_date_argument_is_date(self):
        arguments = terminal.parse_arguments(
            ['-s', '01-01-2022', '-e', '05-01-2022'])
        self.assertIsInstance(arguments.end_date, datetime.date)


if __name__ == '__main__':
    unittest.main()