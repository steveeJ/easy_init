import sys
sys.path.extend('..')
from easy_init import easy_init


def test_defaults():
    args = ['one', 'two', 'three']
    kwargs = {'four': None, 'five': False}
    dummy_object = DummyClass(*args)

    for arg in args:
        assert arg == getattr(dummy_object, arg)
    for k, v in kwargs.items():
        assert v == getattr(dummy_object, k)


def test_explicit():
    args = ['one', 'two', 'three']
    kwargs = {'four': None, 'five': False}
    dummy_object = DummyClass(*args, **kwargs)

    for arg in args:
        assert arg == getattr(dummy_object, arg)
    for k, v in kwargs.items():
        assert v == getattr(dummy_object, k)


def test_mixed():
    args = ['three', 'four']
    kwargs = {'five': False}
    dummy_object = DummyClass('one', 'two',
        *args,  six='six', seven=7, **kwargs)

    for arg in args:
        assert getattr(dummy_object, arg) == arg
    for k, v in kwargs.items():
        assert getattr(dummy_object, k) == v
    assert False == hasattr(dummy_object, 'six')
    assert False == hasattr(dummy_object, 'seven')


class DummyClass(object):
    @easy_init
    def __init__(self, one, two, three, four=None, five=False, *args, **kwargs):
        pass
