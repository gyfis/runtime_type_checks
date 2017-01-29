from runtime_type_checks import runtime_type_checks, RuntimeTypeCheckError

import unittest

from typing import Dict, Tuple, List, Iterable


@runtime_type_checks
def params_with_return_type(name: str, age: int) -> str:
    return "Name: {}; age: {}".format(name, age)


@runtime_type_checks
def params_with_wrong_return_type(name: str, age: int) -> int:
    return "Name: {}; age: {}".format(name, age)


@runtime_type_checks
def params_without_return_type(name: str, age: int):
    return "Name: {}; age: {}".format(name, age)


@runtime_type_checks
def params_with_args(name: str, age: int, *args):
    return "Name: {}; age: {}; {}".format(name, age, ' '.join(args))


@runtime_type_checks
def params_with_kwargs(name: str, age: int, **kwargs):
    return "Name: {}; age: {}; {}".format(name, age, kwargs['foo'])


@runtime_type_checks
def typing_list(l: List):
    return len(l)


@runtime_type_checks
def typing_str_list(l: List[str]):
    return len(l)


@runtime_type_checks
def typing_iterable(l: Iterable):
    return len(l)


class TestArgs(unittest.TestCase):

    def test_primitive_return(self):
        self.assertRaises(RuntimeTypeCheckError, params_with_return_type, 'str', 1.2)
        self.assertRaises(RuntimeTypeCheckError, params_with_return_type, 1, 1)
        self.assertRaises(RuntimeTypeCheckError, params_with_return_type, name='str', age=1.2)
        self.assertRaises(RuntimeTypeCheckError, params_with_return_type, name=1, age=1)

        try:
            params_with_return_type('John', 1)
            params_with_return_type(name='John', age=1)
        except:
            assert False

    def test_primitive_wrong_return(self):
        self.assertRaises(RuntimeTypeCheckError, params_with_wrong_return_type, 'str', 1.2)
        self.assertRaises(RuntimeTypeCheckError, params_with_wrong_return_type, 1, 1)
        self.assertRaises(RuntimeTypeCheckError, params_with_wrong_return_type, name='str', age=1.2)
        self.assertRaises(RuntimeTypeCheckError, params_with_wrong_return_type, name=1, age=1)

    def test_primitive_no_return(self):
        self.assertRaises(RuntimeTypeCheckError, params_without_return_type, 'str', 1.2)
        self.assertRaises(RuntimeTypeCheckError, params_without_return_type, 1, 1)
        self.assertRaises(RuntimeTypeCheckError, params_without_return_type, name='str', age=1.2)
        self.assertRaises(RuntimeTypeCheckError, params_without_return_type, name=1, age=1)

        try:
            params_with_return_type('John', 1)
            params_with_return_type(name='John', age=1)
        except Exception:
            assert False

    def test_args(self):
        self.assertRaises(RuntimeTypeCheckError, params_with_args, 'str', 1.2)
        self.assertRaises(RuntimeTypeCheckError, params_with_args, 'str', 1.2, 'hello', 'my', 'friend')
        self.assertRaises(RuntimeTypeCheckError, params_with_args, 1, 1, 'hello', 'my', 'friend')
        self.assertRaises(RuntimeTypeCheckError, params_with_args, name='str', age=1.2)
        self.assertRaises(RuntimeTypeCheckError, params_with_args, name=1, age=1)

        try:
            params_with_args('John', 1, 'hello', 'my', 'friend')
            params_with_args(name='John', age=1)
        except Exception:
            assert False

    def test_kwargs(self):
        self.assertRaises(RuntimeTypeCheckError, params_with_kwargs, 'str', 1.2, foo='hello')
        self.assertRaises(RuntimeTypeCheckError, params_with_kwargs, 1, 1, foo='hello', bar='my')
        self.assertRaises(RuntimeTypeCheckError, params_with_kwargs, name='str', age=1.2, foo='hello')
        self.assertRaises(RuntimeTypeCheckError, params_with_kwargs, name=1, age=1, foo='hello', bar='my')

        try:
            params_with_kwargs('John', 1, foo='hello')
            params_with_kwargs('John', 1, foo='hello', bar='my')
            params_with_kwargs(name='John', age=1, foo='hello')
            params_with_kwargs(name='John', age=1, foo='hello', bar='my')
        except Exception:
            assert False

    def test_typing_list(self):
        self.assertRaises(RuntimeTypeCheckError, typing_list, 12)
        self.assertRaises(RuntimeTypeCheckError, typing_list, 'hello')

        try:
            typing_list([])
            typing_list(['foo', 12, 'bar', 12.2])
            typing_list(l=[])
            typing_list(l=['foo', 12, 'bar', 12.2])
        except:
            assert False

    def test_typing_iterable(self):
        self.assertRaises(RuntimeTypeCheckError, typing_iterable, 12)
        self.assertRaises(RuntimeTypeCheckError, typing_iterable, 12.2)

        try:
            typing_iterable([])
            typing_iterable('foo')
            typing_iterable(['foo', 12, 'bar', 12.2])
            typing_iterable(l=[])
            typing_iterable(l=['foo', 12, 'bar', 12.2])
        except:
            assert False

    # TODO: support this
    # def test_typing_str_list(self):
    #     self.assertRaises(RuntimeTypeCheckError, typing_str_list, ['foo', 12, 'bar', 12.2])
    #     self.assertRaises(RuntimeTypeCheckError, typing_str_list, [12.2])
    #     self.assertRaises(RuntimeTypeCheckError, typing_str_list, 12)
    #     self.assertRaises(RuntimeTypeCheckError, typing_str_list, 'foo')
    #
    #     try:
    #         typing_str_list([])
    #         typing_str_list(['foo', 'bar'])
    #         typing_str_list(l=[])
    #         typing_str_list(l=['foo', 'bar'])
    #     except:
    #         assert False
