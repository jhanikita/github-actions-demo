from src.maths_operation import add,multiply

def test_add():
    assert add(2,24) == 26
    assert add(-1,1) == 0

def multiply():
    assert multiply(2,3) == 6
    assert multiply(4,2) == 8
    assert multiply(3,0) == 0

