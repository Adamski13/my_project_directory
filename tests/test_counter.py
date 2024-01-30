from lib.counter import *

#Initially reports a zero count
def test_counter_reports_zero():
    counter = Counter()
    assert counter.report() == "Counted to 0 so far."

#Adding a single number to the counter:
def test_adding_a_single_number():
    counter = Counter()
    counter.add(7)
    assert counter.report() == "Counted to 7 so far."

#Adding multiple numbers to the counter:
def test_adding_multiple_numbers():
    counter = Counter()
    counter.add(13)
    counter.add(24)
    assert counter.report() == "Counted to 37 so far."