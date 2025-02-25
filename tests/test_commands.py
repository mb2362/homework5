"""
Unit tests for command classes in the CLI calculator application.
"""

from unittest.mock import patch
import pytest   # pylint: disable=unused-import
from app import App
from app.commands import CommandHandler, CLI
from app.plugins.add import addCommand
from app.plugins.subtract import subtractCommand
from app.plugins.multiply import multiplyCommand
from app.plugins.divide import divideCommand

def test_app_init():
    """Test that the App initializes with a CommandHandler."""
    app = App()
    assert app.command_handler is not None

def test_app_start_menu_command():
    """Test App start method handling a menu command."""
    app = App()
    with patch("builtins.input", side_effect=["menu", "exit"]), patch("builtins.print") as mock_print:
        with pytest.raises(SystemExit):  # Exit after calling 'exit'
            app.start()
    # Verify that the menu command is recognized
    mock_print.assert_any_call("Type 'exit' to exit or 'menu' to enter menu section.")
    mock_print.assert_any_call("Available commands: add, subtract, multiply, divide, menu, exit\n")  # ✅ Correct output
    mock_print.assert_any_call("Commands should be in this format: add 5 3\n")  # ✅ Additional menu info
    mock_print.assert_any_call("Exiting...")  # ✅ Correct exit message

def test_app_invalid_command():
    """Test handling of an invalid command."""
    app = App()
    with patch("builtins.input", side_effect=["unknown", "exit"]), patch("builtins.print") as mock_print:
        with pytest.raises(SystemExit):
            app.start()
    mock_print.assert_any_call("No such command: unknown")

def test_add_command(capfd):
    """Test addition command with valid inputs."""
    command = addCommand()
    command.execute(["5", "3"])
    out, _ = capfd.readouterr()
    assert out == "The result of 5 + 3 is equal to 8.0\n"

def test_subtract_command(capfd):
    """Test subtraction command with valid inputs."""
    command = subtractCommand()
    command.execute(["10", "2"])
    out, _ = capfd.readouterr()
    assert out == "The result of 10 - 2 is equal to 8.0\n"

def test_multiply_command(capfd):
    """Test multiplication command with valid inputs."""
    command = multiplyCommand()
    command.execute(["4", "5"])
    out, _ = capfd.readouterr()
    assert out == "The result of 4 x 5 is equal to 20.0\n"

def test_divide_command(capfd):
    """Test division command with valid inputs."""
    command = divideCommand()
    command.execute(["20", "4"])
    out, _ = capfd.readouterr()
    assert out == "The result of 20 / 4 is equal to 5.0\n"

class DummyCommand(CLI):
    """A dummy command for testing CommandHandler functionality."""
    def execute(self, args):
        super().execute(args)
        print("Dummy executed")

def test_execute_command_success(capfd):
    """Test that a registered command is executed successfully."""
    handler = CommandHandler()
    handler.register_command("dummy", DummyCommand())
    handler.execute_command("dummy")
    out, _ = capfd.readouterr()
    assert "Dummy executed" in out

def test_execute_command_keyerror(capfd):
    """Test that calling an unregistered command prints an error message."""
    handler = CommandHandler()
    handler.execute_command("nonexistent")
    out, _ = capfd.readouterr()
    assert "No such command: nonexistent" in out

def test_add_command_missing_arguments(capfd):
    """Test addCommand with missing arguments."""
    command = addCommand()
    command.execute([])  # No arguments provided
    out, _ = capfd.readouterr()
    assert out == "Usage: add <a> <b>\n"

def test_add_command_length(capfd):
    """Test addCommand with missing arguments."""
    command = addCommand()
    command.execute(["5"])
    out, _ = capfd.readouterr()
    assert out == "Usage: add <a> <b>\n"

def test_add_command_invalid_argument(capfd):
    """Test addCommand with non-numeric argument."""
    command = addCommand()
    command.execute(["5", "b"])
    out, _ = capfd.readouterr()
    assert out == "Invalid number input: 5 or b is not a valid number.\n"

def test_divide_command_length(capfd):
    """Test divideCommand with missing arguments."""
    command = divideCommand()
    command.execute(["5"])
    out, _ = capfd.readouterr()
    assert out == "Usage: divide <a> <b>\n"

def test_divide_command_invalid_argument_1(capfd):
    """Test divideCommand with non-numeric argument."""
    command = divideCommand()
    command.execute(["5", "b"])
    out, _ = capfd.readouterr()
    assert out == "Invalid number input: 5 or b is not a valid number.\n"

def test_divide_command_invalid_argument_2(capfd):
    """Test divideCommand with division by zero."""
    command = divideCommand()
    command.execute(["5", "0"])
    out, _ = capfd.readouterr()
    assert out == "An error occurred: Cannot divide by zero.\n"

def test_multiply_command_missing_arguments(capfd):
    """Test multiplyCommand with missing arguments."""
    command = multiplyCommand()
    command.execute([])  # No arguments provided
    out, _ = capfd.readouterr()
    assert out == "Usage: multiply <a> <b>\n"

def test_multiply_command_length(capfd):
    """Test multiplyCommand with missing arguments."""
    command = multiplyCommand()
    command.execute(["5"])
    out, _ = capfd.readouterr()
    assert out == "Usage: multiply <a> <b>\n"

def test_multiply_command_invalid(capfd):
    """Test multiplyCommand with non-numeric argument."""
    command = multiplyCommand()
    command.execute(["5", "b"])
    out, _ = capfd.readouterr()
    assert out == "Invalid number input: 5 or b is not a valid number.\n"

def test_subtract_command_missing_arguments(capfd):
    """Test subtractCommand with missing arguments."""
    command = subtractCommand()
    command.execute([])  # No arguments provided
    out, _ = capfd.readouterr()
    assert out == "Usage: subtract <a> <b>\n"

def test_subtract_command_length(capfd):
    """Test subtractCommand with missing arguments."""
    command = subtractCommand()
    command.execute(["5"])
    out, _ = capfd.readouterr()
    assert out == "Usage: subtract <a> <b>\n"

def test_subtract_command_invalid(capfd):
    """Test subtractCommand with non-numeric argument."""
    command = subtractCommand()
    command.execute(["5", "b"])
    out, _ = capfd.readouterr()
    assert out == "Invalid number input: 5 or b is not a valid number.\n"

def test_pytest_addoption(pytestconfig):
    """Test that the custom --num_records option is recognized."""
    num_records = pytestconfig.getoption("--num_records")
    assert isinstance(num_records, int)
    assert num_records == 10  # Default value

def test_generated_test_data(test_data):
    """Test that the test_data fixture generates valid test cases."""
    assert isinstance(test_data, list)
    assert len(test_data) > 0  # Should generate at least one case

    a, b, operation, expected_result = test_data[0] # pylint: disable=unused-variable
    assert isinstance(a, int)
    assert isinstance(b, int)
    assert operation in ('add', 'subtract', 'multiply', 'divide')
