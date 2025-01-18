import pytest
from myfile import Fibonacci

def test_passing():
    assert Fibonacci(9) == 34

def test_failing():
    assert Fibonacci(9) == 35