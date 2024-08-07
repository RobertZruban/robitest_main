import pytest
from robitest_main.correlation import calculate_pearson_correlation

def test_positive_correlation():
    result = calculate_pearson_correlation([1, 2, 3], [4, 5, 6])
    assert result == pytest.approx(1.0)

def test_negative_correlation():
    result = calculate_pearson_correlation([1, 0, -1], [-1, 0, 1])
    assert result == pytest.approx(-1.0)

# def test_no_correlation():
#     result = calculate_pearson_correlation([1, 2, 3], [7, 7, 7])
#     assert result == pytest.approx(0.0)

def test_different_lengths():
    with pytest.raises(ValueError):
        calculate_pearson_correlation([1, 2, 3], [4, 5])

def test_insufficient_length():
    with pytest.raises(ValueError):
        calculate_pearson_correlation([1], [4])

def test_zero_denominator():
    with pytest.raises(ValueError):
        calculate_pearson_correlation([1, 1, 1], [2, 2, 2])