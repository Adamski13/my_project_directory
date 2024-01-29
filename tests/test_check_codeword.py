from lib.check_codeword import check_codeword

#if the test is correct, returns: correct
def test_correct_codeword():
        result = check_codeword('horse')
        assert "Correct! Come in."

#if the code is close, returns: close, but nope
def test_mistakenly_close_codeword():
        result = check_codeword('house')
        assert "Close, but nope."

#if the codeword is wrong, returns WRONG!
def test_wrong_codeword():
        result = check_codeword('monkey')
        assert "WRONG!"

#but what if the first letter is correct but last not? Returns: WRONG!
def test_with_right_first_letter_and_wrong_last_letter():
        result = check_codeword('hamster')
        assert "WRONG!"

#if the first letter is wrong but last letter is correct - Returns: WRONG!
def test_with_wrong_first_letter_and_right_last_letter():
        result = check_codeword('snake')
        assert "WRONG!"
        