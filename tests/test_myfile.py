from src.myfile import Fibonacci


def test_passing() -> None:
    assert Fibonacci(9) == 34


def test_failing() -> None:
    assert Fibonacci(9) == 35
