from src.myfile import Fibonacci
import pytest

def test_passing() -> None:
    assert Fibonacci(9) == 34

def test_0_iput() -> None:
    assert Fibonacci(0) == 0

def test_negative_input() -> None:
    with pytest.raises(ValueError):
        Fibonacci(-5)

def test_failing() -> None:
    assert Fibonacci(10) == 55
