import pytest
from biblioteka_wsb.Person import Student

@pytest.fixture
def test_student():
    test_student = Student("Test", "Student", 123456)
    return test_student

def test_get_id(test_student):
    assert test_student.get_id() == 123456


def test_get_name(test_student):
    assert test_student.get_name() == "Test Student"

def test__str__(test_student):
    assert str(test_student) == "Student: Test Student, id: 123456"
