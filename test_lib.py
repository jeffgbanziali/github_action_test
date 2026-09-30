from lib import average

def test_average():
    assert average([1, 2, 3]) == 2.0
    assert average([10, 20, 30, 40]) == 25.0
    assert average([5]) == 5.0