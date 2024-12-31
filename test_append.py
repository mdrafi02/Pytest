import pytest 

#Arrange
@pytest.fixture
def first_entry():
    return "a"

#Arrange
@pytest.fixture
def second_entry():
    return 2

""" Fixtures can request other fixtures """
#Arrange
@pytest.fixture
def order(first_entry, second_entry):
    return [first_entry, second_entry]

# Arrange
@pytest.fixture
def expected_list():
    return ["a",2,"a",3.0]

"""Fixtures are reusable and  A Test/Fixture can request more than one fixture at a time"""

def test_string(order, expected_list):
    #Act
    order.append(3.0)

    #Assert 
    assert order == expected_list

def test_int(order):
    #Act
    order.append(2)

    #Assert
    assert order == ['a',2,2]

""" Fixtures can be requested more than once per test , return values are cached"""
#Act
""" Autouse Fixtures , fixtures you don't have to request"""
@pytest.fixture(autouse=True)
def append_first(order, first_entry):
    return order.append(first_entry)

def test_string_only(order,first_entry):
    #Assert 
    assert order == [first_entry,2,first_entry]

def test_string_and_int(order,first_entry):
    order.append(2)
    assert order == [first_entry, 2,first_entry,2]