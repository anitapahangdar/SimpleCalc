# SimpleCalc — Python Command-Line Calculator

A compact command-line calculator created by **Anita Pahangdar**. It performs the four basic arithmetic operations in a repeatable interactive session.

## Features

- Addition, subtraction, multiplication, and division
- Clear exit command before number entry
- Validation for non-numeric input
- Division-by-zero handling
- Reusable `calculate()` function
- Standard Python `main` entry point
- No external dependencies

## Run locally

Install Python 3.8 or newer, then run:

```bash
python index.py
```

On some systems, use `python3 index.py`.

## Example

```text
SimpleCalc — enter an operation or type 'exit' to quit.

Operation (+, -, *, /, exit): *
Enter the first number: 7
Enter the second number: 6
Result: 42
```

## Project structure

```text
.
├── index.py    # Calculator logic and interactive interface
├── .gitignore  # Python cache and environment exclusions
└── README.md
```

## Possible next steps

- Add exponent, remainder, and square-root operations
- Store a calculation history
- Add unit tests for `calculate()`
- Build a small graphical interface

## Author

**Anita Pahangdar**
