import collections
import unittest
from unittest.mock import patch

from guet.commands.command import *

test_case = collections.namedtuple('TestCase', 'input expected_output explanation')


def create_test_case(input, expected_output, explanation):
    return test_case(input=input, explanation=explanation, expected_output=expected_output)


class TestCommand(unittest.TestCase):

    def test_all_commands_pass_arguments_to_super_constructor(self):
        args = []
        for command_class in Command.__subclasses__():
            command = command_class(args)
            self.assertIsNotNone(command._args)


class TestCommand2(unittest.TestCase):
    class Command2Impl(Command2):
        called = False

        @classmethod
        def help_short(cls):
            pass

        def execute_hook(self):
            self.called = True

        def help(self):
            return 'Help'

    def test_execute_calls_implementation_command_hook(self):
        command = self.Command2Impl(['command2', 'arg'])
        command.execute()
        self.assertTrue(command.called)

    @patch('builtins.print')
    def test_prints_help_message_when_no_args_given_with_appended_newline(self,
                                                    mock_print):
        command = self.Command2Impl(['command2'])
        command.execute()
        mock_print.assert_called_with('Help\n')

    @patch('builtins.print')
    def test_does_not_print_help_message_when_no_args_given_if_that_is_valid_for_command(self,
                                                                                         mock_print):
        command = self.Command2Impl(['command2'], args_needed=False)
        mock_print.assert_not_called()
