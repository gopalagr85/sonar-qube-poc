import pytest
from src.good_code import Calculator as GoodCalculator, main
from src.bad_code import Calculator as BadCalculator


# Tests for good code
def test_good_add():
    calc = GoodCalculator()
    assert calc.add(5, 3) == 8

def test_good_subtract():
    calc = GoodCalculator()
    assert calc.subtract(10, 4) == 6

def test_good_divide():
    calc = GoodCalculator()
    assert calc.divide(8, 2) == 4
    assert calc.divide(5, 0) is None

def test_main():
    val = main()
    assert val == True


# Tests for bad code
def test_bad_add():
    calc = BadCalculator()
    assert calc.add(5, 3) == 8

def test_bad_subtract():
    calc = BadCalculator()
    assert calc.subtract(10, 4) == 6

def test_bad_divide():
    calc = BadCalculator()
    # This will raise ZeroDivisionError
    import pytest
    with pytest.raises(ZeroDivisionError):
        calc.divide(5, 0)