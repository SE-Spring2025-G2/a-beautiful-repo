# a-beautiful-repo

![Python](https://img.shields.io/badge/Made%20With-Python-blue) ![License: MIT](https://img.shields.io/badge/License-MIT-green) [![Proj1 Tests](https://github.com/SE-Spring2025-G2/a-beautiful-repo/actions/workflows/main.yml/badge.svg)](https://github.com/SE-Spring2025-G2/a-beautiful-repo/actions/workflows/main.yml) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14721778.svg)](https://doi.org/10.5281/zenodo.14721778) 
![Flake8](https://img.shields.io/badge/style-flake8-blue)
![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)
![Checked with mypy](https://img.shields.io/badge/mypy-checked-blue)
![Codecov](https://img.shields.io/codecov/c/github/SE-Spring2025-G2/a-beautiful-repo)

Welcome to "A Beautiful Repo," created as part of the **Spring 2025 Software Engineering** course.

---

## Table of Contents

- [Overview](#overview)
- [Documentation](#documentation)
  - [myfile.py](#myfilepy)
  - [test_myfile.py](#test_myfilepy)
- [Contributing](#contributing)
- [Authors](#authors)
- [License](#license)

---

## Project Overview

This repository contains the implementation and testing of a recursive Fibonacci function. The structure tries to adhere to professional software engineering principles with proper documentation, unit testing, and version control.

### Features

- **Recursive Fibonacci Function**: Computes the nth Fibonacci number.
- **Unit Tests**: Ensures correctness and edge case handling.
- **CI/CD Integration**: GitHub Actions workflow for automated testing.
- **Style Checker**: This project uses Flake8 to ensure consistent style checking.
- **Code Formatter**: Black is being used to check for standard code formatting.
- **Syntax Checker**: MyPy is being used for the syntax checking.
- **Code coverage**: All code coverage checking is done by Codecov.
- **Security Checking**: All security checks done by Bandit.
---

## Documentation

### myfile.py

**Purpose:** Implements a recursive Fibonacci sequence generator.

#### Functions:

1. **`Fibonacci(n)`**:
   - **Description**: Computes the nth Fibonacci number using recursion.
   - **Parameters**:
     - `n` (int): The position of the Fibonacci sequence to compute. Must be non-negative.
   - **Returns**:
     - Fibonacci number at position `n`.
   - **Exceptions**:
     - Raises `ValueError` for invalid input (e.g., `n < 0`).
   - **Example Usage**:
     ```python
     Fibonacci(10)  # Output: 55
     ```

### test_myfile.py

**Purpose:** Contains unit tests for the `Fibonacci` function.

#### Tests:

1. **Test Cases:**
   - Valid inputs (e.g., `Fibonacci(0)`, `Fibonacci(1)`, `Fibonacci(10)`).
   - Edge cases (e.g., `Fibonacci(-1)` raises `ValueError`).
   - Performance for larger values.

---

## Contributing

We welcome contributions to this repository. Join the [**Discord Chat Channel**](https://discord.com/channels/1322756098582904842/1327005283335278662) for discussions, feedback, and collaboration.

### Steps to Contribute:
1. Fork the repository.
2. Clone your fork locally.
3. Create a feature branch.
4. Commit and push your changes.
5. Submit a pull request.

---

## Authors

- **Ayush Phatak** - NC State University  
- **Keyur Gondhalekar** - NC State University  
- **Ayush Gala** - NC State University  

---

## License

This project is licensed under the MIT License. See [LICENSE.md](LICENSE.md) for details.

---

## Feedback

Your feedback is valuable to us. Please open an issue or join our [Discord Chat Channel](https://discord.com/channels/1322756098582904842/1327005283335278662) to share your thoughts.
