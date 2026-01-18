#smoke test
from test_leapyear_Calculator import is_leap_year

def test_leapyear_rules():
    assert is_leap_year(2024) is True
    assert is_leap_year(1997) is False
    assert is_leap_year(2012) is True
    assert is_leap_year(2023) is False

    

    