# Literal Dict

`literal-dict` is a Python utility that allows for the creation of dictionary objects with a syntax reminiscent of JavaScript object notation. This tool is particularly useful for developers looking to streamline their code by reducing the verbosity commonly associated with dictionary creation in Python.

## Features

- **Intuitive Variable Inclusion**: Create Python dictionaries using a syntax similar to JavaScript objects: automatically uses variable names as keys, simplifying the process of dictionary creation.
- **Flexible Dictionary Implementations**: Supports custom dictionary implementations, enabling behaviors like ordered dictionaries, default dictionaries, dot dictionaries, and more.
- **Various Python Distribution Supports**: This package is tested under almost every popular python implementations.

## Installation

```bash
pip install literal-dict
```

## Usage

### Basic Dictionary Creation

Start by importing `DictBuilder` from the package:

```py
from literal_dict import DictBuilder
```

Create a `DictBuilder` instance:

```py
d = DictBuilder()
```

Now, you can create dictionaries with a simplified syntax:

```py
name = "Muspi Merol"
age = 20

user = d[name, age, "active": True]
print(user)  # Output: {'name': 'Muspi Merol', 'age': 20, 'active': True}
```

### Using Custom Dictionary Implementations

`DictBuilder` allows specifying a custom dict-like type:

#### Example with `types.SimpleNamespace`

Using `SimpleNamespace` from the `types` module allows for attribute-style access to dictionary keys. This can make your code cleaner and more readable in some cases.

```python
from types import SimpleNamespace

from literal_dict import DictBuilder

d = DictBuilder(lambda dict: SimpleNamespace(**dict))

name = "Muspi Merol"
email = "me@promplate.dev"

person = d[name, email]
print(person.name)  # Output: Muspi Merol
print(person.email)  # Output: me@promplate.dev
```

Note: When using `SimpleNamespace`, the returned object is not a dictionary but an instance of `SimpleNamespace`, which allows for dot-notation access to the attributes.

#### Example with `collections.defaultdict`

```py
from collections import defaultdict
from functools import partial

from literal_dict import DictBuilder

d = DictBuilder(partial(defaultdict, int))

a = 1

obj = d[a, "b":2]
print(obj["c"])  # Output: 0, since 'c' does not exist, it returns the default int value
```

## Conclusion

The `Literal Dict Builder` offers a succinct and intuitive way to create dictionaries in Python, drawing inspiration from JavaScript's object notation. Its support for custom dictionary implementations adds a layer of flexibility, allowing developers to tailor their data structures to fit their needs.
