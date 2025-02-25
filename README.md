# Advanced Calculator

## Overview
The **Advanced Calculator** is a modular and object-oriented Python package for performing high-precision arithmetic operations. It supports addition, subtraction, multiplication, and division using Python's `decimal.Decimal` class for accuracy.

## Features
- Perform precise arithmetic calculations.
- Store and retrieve calculation history.
- Support for flexible and reusable calculation objects.
- Unit tests using `pytest`.

## Project Structure
```
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
Example of using the calculator:
```python
from calculator import Calculator
from decimal import Decimal

result = Calculator.add(Decimal('10.5'), Decimal('5.5'))
print(f"Addition Result: {result}")
```

## Running Tests
Run the tests using `pytest`:
```bash
pytest tests/
```