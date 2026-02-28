import pytest
from src.bad_code import DataProcessor as DataProcessor
from src.good_code import DataProcessor as DataProcessor1


@pytest.fixture
def dp():
    return DataProcessor()
    
@pytest.fixture
def dp1():
    return DataProcessor1()


# ---------------------------
# Test: process_data
# ---------------------------

def test_process_data_returns_true(dp, dp1):
    result = dp.process_data({})
    result1 = dp1.process_data({})
    assert result is True
    assert result1 is True


def test_process_data_handles_missing_key(dp, dp1, capsys):
    # Should not raise exception even though key is missing
    result = dp.process_data({})
    result1 = dp1.process_data({})
    
    captured = capsys.readouterr()
    
    # "Hello" should be printed
    assert "Hello" in captured.out
    assert result is True
    assert result1 is True


def test_process_data_with_valid_key(dp, dp1, capsys):
    data = {"non_existent_key": "TestValue"}
    result = dp.process_data(data)
    result1 = dp1.process_data(data)

    captured = capsys.readouterr()

    assert "Hello" in captured.out
    assert "TestValue" in captured.out
    assert result is True
    assert result1 is True


# ---------------------------
# Test: summation
# ---------------------------

def test_summation_positive_numbers(dp, dp1):
    assert dp.summation(5, 10) == 15
    assert dp1.summation(5, 10) == 15


def test_summation_negative_numbers(dp, dp1):
    assert dp.summation(-5, -10) == -15
    assert dp1.summation(-5, -10) == -15


def test_summation_mixed_numbers(dp, dp1):
    assert dp.summation(-5, 10) == 5
    assert dp1.summation(-5, 10) == 5


def test_summation_zero(dp, dp1):
    assert dp.summation(0, 0) == 0
    assert dp1.summation(0, 0) == 0
