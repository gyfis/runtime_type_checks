import logging
import inspect
import typing


class RuntimeTypeCheckError(Exception):
    pass


def runtime_type_checks(func):
    """
    Decorator that performs a runtime check of passed and returned types.
    :param func: function to be decorated (valid Python 3.5+ function with full typing hints support)
    :return: decorated function which is provided with runtime type checks
    """

    def func_wrapper(*args, **kwargs):
        # get type hints of the
        type_hints = typing.get_type_hints(func)

        func_spec = inspect.getfullargspec(func)

        # check *args
        args_names = func_spec.args
        for i, (key, value) in enumerate(zip(args_names, args)):
            if not isinstance(value, type_hints[key]):
                raise RuntimeTypeCheckError('Positional argument #{} ({}) of type {} does not match required'
                                            'type {}'.format(i, key, type(value), type_hints[key]))

        # check **kwargs
        for key, value in kwargs.items():
            if key in type_hints:
                if not isinstance(value, type_hints[key]):
                    raise RuntimeTypeCheckError('{} of type {} does not match required type {}'.format(key,
                                                                                                       type(value),
                                                                                                       type_hints[key]))

        # return type if specified
        result = func(*args, **kwargs)
        try:
            return_type = func_spec.annotations['return']
            if not isinstance(result, return_type):
                raise RuntimeTypeCheckError('Returned value of type {} does not match required type'
                                            'return {}'.format(type(result), return_type))
        except KeyError:
            pass

        return result

    return func_wrapper
