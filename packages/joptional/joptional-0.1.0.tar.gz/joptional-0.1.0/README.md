# pyoptional

Java-style Optionals for Python.

## Installation

Simply install this package with your favourite package manager:

    pip install pyoptional

or

    poetry install pyoptional

## Usage

The `Optional` class is a generic class that can be used to wrap a value that may or may not be `None`.
Its functionality is roughly equivalent to Java's `Optional` class. For example:

```java
Optional<String> opt = Optional.of("Hello, world!");
opt.ifPresent(System.out::println);
```

turns to the following Python code:

```python
opt = Optional[str].of("Hello, world!")
opt.if_present(print)
```

Of course, type annotations in Python are optional (no pun intended),
so you can simply write `Optional.of("Hello, world!")` if you prefer.
