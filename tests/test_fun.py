from tests import _PATH_DATA


def adder(a: float, b: float) -> float:
    return a + b


def test_adder() -> None:
    assert adder(2, 3) == 5
    assert adder(-1, 1) == 0
    assert adder(0, 0) == 0
