import pytest
import pdb
from methods.various_methods import VariousMethods


def setup_function(function):
    print('Start-up test')


def teardown_function(function):
    print('Shut-down test')


def test_atlas():
    ''' Test: if the integer is multiple of 3
    return the string “Atlas'''
    msg = 'integer multiple of 3 shall return "Atlas"'
    expected = 'Atlas'
    integers_to_test = [9, 18, 87]
    for integer in integers_to_test:
        test = VariousMethods().ConvertToAtlasCopcoString(integer)
        assert test == expected


def test_copco():
    ''' Test: if the integer is multiple of five it will
    return the string “Copco'''
    msg = 'integer multiple of 5 shall return "Copco"'
    expected = 'Copco'
    integers_to_test = [5, 65, 100]
    for integer in integers_to_test:
        test = VariousMethods().ConvertToAtlasCopcoString(integer)
        assert test == expected


def test_atlas_copco():
    ''' Test: if the integer is multiple of three and five it will
    return the string “AtlasCopco”'''
    msg = 'integer multiple of 5 and 3 shall return "AtlasCopco"'
    expected = 'AtlasCopco'
    integers_to_test = [30, 60, 90]
    for integer in integers_to_test:
        test = VariousMethods().ConvertToAtlasCopcoString(integer)
        assert test == expected


def test_string_not_multiple_of_five_or_three():
    ''' Test: if the integer is inside range 1-100 but not multiple of 3 or 5
    then return the integer as string'''
    msg = 'return string of the integer"'
    test_data = [2, 4, 2.6]
    expected_data = ['2', '4', '2.6']
    for data, expected in zip(test_data, expected_data):
        test = VariousMethods().ConvertToAtlasCopcoString(data)
        assert test == expected


def test_outside_range():
    ''' Test: if values outside of the range 1-100
    that the method throw a value exception.”'''
    integers_outside_range = [-1, 102, -5, 101]
    for integer in integers_outside_range:
        with pytest.raises(ValueError):
            test = VariousMethods().ConvertToAtlasCopcoString(integer)
