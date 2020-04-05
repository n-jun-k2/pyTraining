import pytest
import fizzbuzz.example1 as ex1

def test_function():
    """ fizzbuzz()の戻り値を検証する。"""
    assert ex1.fizzbuzz(3) == 'Fizz', '戻り値が一致しません。'