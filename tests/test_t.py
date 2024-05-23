import t
import pytest

@pytest.mark.parametrize(
        ('input_n', 'expected'),
        ((5,25),
         (3.,9.))
)
def test_square_param(input_n,expected):
    assert t.square(input_n) == expected


# def test_square():
#     assert t.square(5) == 25


# def test_square_float():
#     assert t.square(3.) == 9.