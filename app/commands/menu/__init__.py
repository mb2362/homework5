# Menu
from app.commands import CLI

class menuCommand(CLI):
    def execute(self, args):
        print("Available commands: add, subtract, multiply, divide, menu, exit\n")
        print("Commands should be in this format: add 5 3\n")