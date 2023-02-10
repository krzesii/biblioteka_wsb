import pytest
from biblioteka_wsb.Person import Teacher

@pytest.fixture
def test_teacher():
    test_teacher = Teacher("Test", "Teacher", 123456)
    return test_teacher

def test_get_id(test_teacher):
    assert test_teacher.get_id() == 123456


def test_get_name(test_teacher):
    assert test_teacher.get_name() == "Test Teacher"

def test__str__(test_teacher):
    assert str(test_teacher) == "Teacher Test Teacher with id 123456"