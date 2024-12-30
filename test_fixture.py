import pytest

@pytest.fixture
def numbers():
    a = 10
    b = 20
    c = 30
    return [a,b,c]

@pytest.mark.xfail
def test_method1(numbers):
    assert numbers[0] == 20

@pytest.mark.skip
def test_method2(numbers):
    assert numbers[1] == 20

def test_method3(numbers):
    assert numbers[2] == 30