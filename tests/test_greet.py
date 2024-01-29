from lib.greet import greet

def test_given_name():
    result = greet('Adam')
    assert result == "Hello, Adam!"