from unittest.mock import patch
from tasks import *

def test_input_list():
    with patch('builtins.input', side_effect=['']):
        assert input_list() == []

    with patch('builtins.input', side_effect=['a', '3' , '']):
        assert input_list() == ['a', '3']

def test_season():
    season_dict = (
        'Зима', 'Зима',
        'Весна', 'Весна', 'Весна',
        'Лето', 'Лето', 'Лето',
        'Осень', 'Осень', 'Осень',
        'Зима'
    )
    for i, j in zip(range(13), season_dict):
        assert season(i+1) == j

def test_fib():
    assert fib(0) == 0
    assert fib(1) == 0
    assert fib(2) == [0,1]
    assert fib(4) == [0,1,1,2]
    assert fib(6) == [0,1,1,2,3,5]

def test_number_identical_elements():
    with patch('builtins.input', side_effect=['1', 'qwe', '1', '42', 'qwe', '1', '']):
        assert number_identical_elements() == {
            '1': 3,
            'qwe': 2,
            '42': 1
        }

def test_mean_input():
    assert mean_input([1,2,3,4,5]) == 3
    assert mean_input([0]) == 0

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(10) == False

def test_longest_frequently_used():
    with patch('builtins.input', side_effect=['asf sdfs sdfsdf 23e ad as as as as as sdf 55']):
        assert longest_frequently_used() == ('sdfsdf', 'as')
