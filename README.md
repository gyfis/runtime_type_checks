# Python Runtime Type Checks

[![Build Status](https://api.travis-ci.org/petrbel/runtime_type_checks.svg?branch=master)](https://travis-ci.org/petrbel/runtime_type_checks)

With Python3.5+ `typing` module, one may use simple `@runtime_type_checks` decorator in order to perform hard
runtime checks of the passed parameters types and function return value type.

*Disclaimer: this approx. 1.5 hour project, don't expect anything great or well tested.*

## Installation
So far, directly from GithHub, in near future via `pip`.

## Usage
```python
from runtime_type_checks import runtime_type_checks, RuntimeTypeCheckError

@runtime_type_checks
def get_personal_info(name: str, age: int) -> str:
    return "Name: {}; age: {}".format(name, age)

get_personal_info("John", 28)  # OK
get_personal_info(name="John", age=28)  # OK
get_personal_info("John", age=28)  # OK
get_personal_info("John", 28.5)  # RuntimeTypeCheckError
```

## Applying the Decorator to All Function in the Module
[External link](http://code.activestate.com/recipes/577742-apply-decorators-to-all-functions-in-a-module/)

## Contribution
If you like the decorator, please consider contributing to the project as there are many issues to resolve.
Please refer to the Progress section in order to figure out what is required.

How to contribute:
1. Make a fork
2. Add changes
3. If possible, add tests for your changes
4. Submit a pull request :)

## Progres
- [x] primitive types (e.g. `int`, `string`, ...)
- [x] `typing` types without `Generics` (e.g. `Iterable`, not `Iterable[str]`)
- [ ] test own classes
- [ ] test all `typing` modules
- [ ] test `NewType`
- [ ] test `Callable`
- [ ] test type aliases
- [ ] support nested types (not only `Iterable` but also `Iterable[str]` with deep type checks
- [ ] test class methods
- [ ] test static methods
- [ ] test (and support) `Generics`
- [ ] test `Any`
- [ ] deploy to PYPI
- [x] Travis-CI
- [ ] write better readme including tutorials, external resources etc.

## Thanks
[Tomas Hromada @gyfis](https://github.com/gyfis) for setting up the unit tests and overall support.
