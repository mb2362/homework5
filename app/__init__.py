# APP
from app.commands import CommandHandler
from app.commands.add import addCommand
from app.commands.subtract import subtractCommand
from app.commands.multiply import multiplyCommand
from app.commands.divide import divideCommand
from app.commands.menu import menuCommand
from app.commands.exit import exitCommand

class App:
    def __init__(self):
        self.command_handler = CommandHandler()

    def start(self):
        # Register arithmetic commands
        self.command_handler.register_command("add", addCommand())
        self.command_handler.register_command("subtract", subtractCommand())
        self.command_handler.register_command("multiply", multiplyCommand())
        self.command_handler.register_command("divide", divideCommand())
        # Register additional commands
        self.command_handler.register_command("menu", menuCommand())
        self.command_handler.register_command("exit", exitCommand())

        print("Type 'exit' to exit or 'menu' to enter menu section.")
        while True:
            cmd_input = input(">>> ").strip().split()
            if not cmd_input:
                continue
            cmd_name = cmd_input[0].lower()
            args = cmd_input[1:]
            if cmd_name in self.command_handler.commands:
                self.command_handler.commands[cmd_name].execute(args)
            else:
                print(f"No such command: {cmd_name}")