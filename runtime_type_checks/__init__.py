import logging
import inspect
import typing


class RuntimeTypeCheckError(TypeError):
    pass


_UNINSTANTIABLE = [typing.TypeVar, typing.UnionMeta, typing.TupleMeta, typing.CallableMeta]


def _type_eq(value, value_type):
    value_type_class = value_type.__class__
    if value_type_class in _UNINSTANTIABLE:
        if value_type_class == typing.TypeVar:
            type_var_constraints = value_type.__constraints__

            # empty TypeVar matches everything
            if not type_var_constraints:
                return True

            if not any(_type_eq(value, constraint)
                       for constraint
                       in type_var_constraints):
                return False
            return True

        if value_type_class == typing.TupleMeta:
            if not isinstance(value, tuple):
                return False

            tuple_params = value_type.__tuple_params__
            if not tuple_params:
                return True

            if not hasattr(value, '__iter__'):
                return False

            if len(value) != len(tuple_params):
                return False

            if not all(_type_eq(inner_value, inner_value_type)
                       for inner_value, inner_value_type
                       in zip(value, value_type.__tuple_params__)):
                return False

            return True

        if value_type_class == typing.UnionMeta:
            union_constraints = value_type.__union_params__

            if not union_constraints:
                return True

            if not any(_type_eq(value, constraint)
                       for constraint
                       in union_constraints):
                return False
            return True

    else:
        if not isinstance(value, value_type):
            return False

    return True


def _validate_types(value, value_type, error_message):
    if not _type_eq(value, value_type):
        raise RuntimeTypeCheckError(error_message)


def runtime_type_checks(func):
    """
    Decorator that performs a runtime check of passed and returned types.
    :param func: function to be decorated (valid Python 3.5+ function with full typing hints support)
    :return: decorated function which is provided with runtime type checks
    """

    def func_wrapper(*args, **kwargs):
        # get type hints of the function
        type_hints = typing.get_type_hints(func)

        func_spec = inspect.getfullargspec(func)

        # check *args
        args_names = func_spec.args
        for i, (key, value) in enumerate(zip(args_names, args)):
            _validate_types(value, type_hints[key],
                            error_message='Positional argument #{} ({}) of type {} does not match required'
                                          'type {}'.format(i, key, type(value), type_hints[key]))

        # check **kwargs
        for key, value in kwargs.items():
            if key in type_hints:
                _validate_types(value, type_hints[key],
                                error_message='{} of type {} does not match required type {}'.format(key,
                                                                                                     type(value),
                                                                                                     type_hints[key]))

        # return type if specified
        result = func(*args, **kwargs)
        if 'return' in func_spec.annotations:
            return_type = func_spec.annotations['return']
            _validate_types(result, return_type,
                            error_message='Returned value of type {} does not match required type'
                                          'return {}'.format(type(result), return_type))

        return result

    return func_wrapper
