from runtime_type_checks import runtime_type_checks, RuntimeTypeCheckError

import unittest

from typing import Dict, Tuple, List, Iterable, Union, TypeVar


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


@runtime_type_checks
def typing_tuple(t: Tuple):
    return t


@runtime_type_checks
def typing_str_tuple(t: Tuple[str]):
    return t


@runtime_type_checks
def typing_primitive_tuple(t: Tuple[str, int, list]):
    return t


@runtime_type_checks
def typing_combined_tuple(t: Tuple[Tuple[str, int], Tuple[str, int]]):
    return t


@runtime_type_checks
def typing_primitive_union(t: Union[int, str]):
    return t


# Union flattens = Union[Union[str, int], Union[str, int]] is the same as Union[str, int]
@runtime_type_checks
def typing_combined_union(t: Union[Union[int, str], Union[int, str]]):
    return t


blank_type = TypeVar('T')
primitive_type = TypeVar('T', int, str)


@runtime_type_checks
def typing_blank_type_var(t: blank_type):
    return t


@runtime_type_checks
def typing_primitive_type_var(t: primitive_type):
    return t


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

    def test_typing_tuple(self):
        self.assertRaises(RuntimeTypeCheckError, typing_tuple, 10)
        self.assertRaises(RuntimeTypeCheckError, typing_tuple, [])

        try:
            typing_tuple(())
            typing_tuple((1, 2, 3))
            typing_tuple(('foo',))
        except:
            assert False

    def test_typing_str_tuple(self):
        self.assertRaises(RuntimeTypeCheckError, typing_str_tuple, ())
        self.assertRaises(RuntimeTypeCheckError, typing_str_tuple, (10, ))
        self.assertRaises(RuntimeTypeCheckError, typing_str_tuple, ('a', 'b'))

        try:
            typing_str_tuple(('a', ))
        except:
            assert False

    def test_typing_primitive_tuple(self):
        self.assertRaises(RuntimeTypeCheckError, typing_primitive_tuple, ('a', 10))
        self.assertRaises(RuntimeTypeCheckError, typing_primitive_tuple, ('a', 10, 'a'))

        try:
            typing_primitive_tuple(('a', 10, ['items']))
        except:
            assert False

    def test_typing_combined_tuple(self):
        self.assertRaises(RuntimeTypeCheckError, typing_combined_tuple, ((), ()))
        self.assertRaises(RuntimeTypeCheckError, typing_combined_tuple, (('a',), ('a', 10)))
        self.assertRaises(RuntimeTypeCheckError, typing_combined_tuple, (('a', 10), ('a', 'a')))
        self.assertRaises(RuntimeTypeCheckError, typing_combined_tuple, (('a', 'a'), ('a', 10)))

        try:
            typing_combined_tuple((('a', 10), ('a', 10)))
        except:
            assert False

    def test_typing_union(self):
        self.assertRaises(RuntimeTypeCheckError, typing_primitive_union, [])
        self.assertRaises(RuntimeTypeCheckError, typing_primitive_union, ())
        self.assertRaises(RuntimeTypeCheckError, typing_primitive_union, None)

        try:
            typing_primitive_union('a')
            typing_primitive_union(10)
            typing_combined_union('a')
            typing_combined_union(10)
        except:
            assert False

    def test_typing_blank_type_var(self):
        try:
            typing_blank_type_var('a')
            typing_blank_type_var([])
            typing_blank_type_var(())
        except:
            assert False

    def test_typing_primitive_type_var(self):
        self.assertRaises(RuntimeTypeCheckError, typing_primitive_type_var, ())
        self.assertRaises(RuntimeTypeCheckError, typing_primitive_type_var, [])

        try:
            typing_primitive_type_var('a')
            typing_primitive_type_var(10)
        except:
            assert False


if __name__ == '__main__':
    unittest.main()
