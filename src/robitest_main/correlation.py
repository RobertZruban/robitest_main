from typing import List
import math

def calculate_pearson_correlation(x: List[float], y: List[float]) -> float:
    """
    Calculate the Pearson correlation coefficient between two lists of numbers.

    Parameters
    ----------
    x : List[float]
        The first list of numbers.
    y : List[float]
        The second list of numbers.

    Returns
    -------
    float
        The Pearson correlation coefficient between the two lists.

    Raises
    ------
    ValueError
        If the input lists are of different lengths or if their length is less than 2.

    Examples
    --------
    >>> calculate_pearson_correlation([1, 2, 3], [4, 5, 6])
    1.0

    >>> calculate_pearson_correlation([1, 0, -1], [-1, 0, 1])
    -1.0
    """
    if len(x) != len(y):
        raise ValueError("The input lists must have the same length.")
    if len(x) < 2:
        raise ValueError("The input lists must have at least two elements.")

    n = len(x)
    
    sum_x = sum(x)
    sum_y = sum(y)
    
    sum_x_sq = sum(xi ** 2 for xi in x)
    sum_y_sq = sum(yi ** 2 for yi in y)
    
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))
    
    numerator = n * sum_xy - sum_x * sum_y
    denominator = math.sqrt((n * sum_x_sq - sum_x ** 2) * (n * sum_y_sq - sum_y ** 2)) 
    if denominator == 0:
        raise ValueError("Denominator in correlation calculation is zero.")
    
    return numerator / denominator

# Example usage:
if __name__ == "__main__":
    x = [1, 2, 3]
    y = [4, 5, 6]
    correlation = calculate_pearson_correlation(x, y)
    print(f"Pearson correlation coefficient: {correlation}")
