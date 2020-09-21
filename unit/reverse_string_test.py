import pytest
from methods.various_methods import VariousMethods


def setup_function(function):
    print('Start-up test')


def teardown_function(function):
    print('Shut-down test')


def test_reverse_string():
    ''' Test: return a string reversed'''
    msg = 'Reversed string'
    expected = 'dadrheM'
    test = VariousMethods().ReverseString('Mehrdad')
    assert test == expected


def test_reverse_string_empty():
    ''' Test: empty string gives value exception'''
    with pytest.raises(ValueError):
        test = VariousMethods().ReverseString("")


def test_reverse_string_none():
    ''' Test: None gives value exception'''
    with pytest.raises(ValueError):
        test = VariousMethods().ReverseString(None)
