# Test Package

This is a simple example of how to create a Python package.

## Installation

Run `pip install yidas-TestPackage`

## Structure

```
packaging_tutorial/
├── LICENSE
├── pyproject.toml
├── README.md
├── src/
│   └── TestPackage_yidas/
│       ├── __init__.py
│       └── example.py
└── tests/
```

`example.py`:

```python
# myclass.py
class TestClass:
    def greet(self):
        return "Hello, world!"
```

`pyproject.toml`

```
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "TestPackage_yidas"
...
```

## Usage

```python
# from stress_testing import StressTesting
from TestPackage_yidas import example

def main():
    obj = example.TestClass()
    print(obj.greet())

main()
```