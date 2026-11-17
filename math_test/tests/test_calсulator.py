import pytest
from math_test.sum_calculator import add_numbers

@pytest.fixture(
    params=[
        ((2,2),4), # 1. Сложение двух простых положительных чисел
        ((10,25),35),
        ((10,-8,6),8),  # 2. Сложение трех и более чисел с разными знаками
        ((-5,-9,3,7),-4),
        ((0,0,0),0),  # 3. Сложение нескольких чисел, включая нули
        ((0,7,-7,0),0),
        ((5,0,15),20),
    ],
    ids=[
        "two_positive_small",
        "two_positive_large",
        "three_mixed",
        "four_mixed",
        "all_zeros",
        "mixed_with_zeros_sum_zero",
        "positive_with_zero",
    ],
)
def numbers_data(request):
    return request.param

def test_add_numbers(numbers_data):
    numbers, expected_result = numbers_data
    assert add_numbers(*numbers) == expected_result
