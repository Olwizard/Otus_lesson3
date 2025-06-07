import pytest

from src.modul_func import sum_end

def test_sum_array():
    assert sum_end([1, 2, 3]) == 6
    assert sum_end([1.5, 2.3, 1]) == 4.8