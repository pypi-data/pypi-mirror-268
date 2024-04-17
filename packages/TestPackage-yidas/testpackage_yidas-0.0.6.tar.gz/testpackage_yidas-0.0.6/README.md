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
def greet():
    return "Hello, world!"
```

`TestClass.py`:

```python
class TestClass:
    def greet(self):
        return "Hello, world!"
```

`__init__.py`:

```python
# Autoload (TestClass.TestClass => TestClass)
from .TestClass import TestClass
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
from TestPackage_yidas import example
from TestPackage_yidas import TestClass

print(example.greet())
obj = TestClass()
print(obj.greet())
```