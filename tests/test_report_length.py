from lib.report_length import report_length

#testing given length. Returns lenghth of given string in number of characters.
def test_length():
    result = report_length('Hello world!')
    assert f"This string was 12 characters long"


#what if input is none? Returns This string was 0 chracters long.
def test_if_input_is_none():
    result = report_length('')
    assert f"This string was 0 characters long"

#what if input is integer? You would need to modify the original function to handle this.
