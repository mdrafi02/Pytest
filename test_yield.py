import pytest 

def test_bar(fix_w_yield1, fix_w_yield2):
    print("test bar")

@pytest.fixture
def fix_w_yield1():
    yield 
    print("after yield1")

@pytest.fixture
def fix_w_yield2():
    yield
    print("after yield2")

