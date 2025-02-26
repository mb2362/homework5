# Advanced Calculator

## Overview
The **Advanced Calculator** is a modular and object-oriented Python package for performing high-precision arithmetic operations. It supports addition, subtraction, multiplication, and division using Python's `decimal.Decimal` class for accuracy.

## Features
- Perform precise arithmetic calculations.
- Store and retrieve calculation history.
- Support for flexible and reusable calculation objects.
- Modular plugin structure for extended functionality.
- Unit tests using `pytest`.

## Project Structure
```
app/
│── commands/                # CLI command handler
│── plugins/                 # Plugins directory
│   ├── add/                 # Addition plugin
│   │   ├── __init__.py
│   ├── subtract/            # Subtraction plugin
│   │   ├── __init__.py
│   ├── multiply/            # Multiplication plugin
│   │   ├── __init__.py
│   ├── divide/              # Division plugin
│   │   ├── __init__.py
│   ├── menu/                # Menu plugin
│   │   ├── __init__.py
│   ├── exit/                # Exit plugin
│   │   ├── __init__.py
│   ├── plugins_manager.py   # Plugin loader

│
calculator/
│── __init__.py          # Initializes the Calculator class
│── calculations.py      # Manages calculation history
│── calculation.py       # Defines a Calculation object
│── operations.py        # Implements basic arithmetic operations
│
tests/
│── test_calculation.py  # Unit tests for Calculation class
│── test_calculations.py # Unit tests for history management
│── test_calculator.py   # Unit tests for Calculator interface
│── test_commands.py     # Unit tests for CLI commands
│── test_operation.py    # Unit tests for arithmetic operations
│
README.md                # Project documentation
```

## Installation
Ensure you have Python 3 installed. Clone the repository and navigate into the project directory:
```bash
git clone <repository-url>
cd advanced-calculator
```

## Usage
Example of using the calculator in Python:
```python
from calculator import Calculator
from decimal import Decimal

result = Calculator.add(Decimal('10.5'), Decimal('5.5'))
print(f"Addition Result: {result}")
```

## Plugin System
The **plugins branch** introduces a flexible plugin system for extending functionality. To use plugins:

```bash
python -m app.plugins.add 10 5
python -m app.plugins.subtract 15 3
python -m app.plugins.multiply 4 6
python -m app.plugins.divide 20 5
```

## Running Tests
Run the tests using `pytest`:
```bash
pytest tests/
```
