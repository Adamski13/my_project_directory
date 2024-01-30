from lib.gratitudes import *

#Test for initial empty list. Returns Be grateful for:
def test_initial_output_is_empty_list():
    gratitudes = Gratitudes()
    assert gratitudes.format() == "Be grateful for: "

#Test when there's only one gratitude added to the list.
def test_output_when_only_one_gratitude_added_to_the_list():
    gratitudes = Gratitudes()
    gratitudes.add("being alive")
    assert gratitudes.format() == "Be grateful for: being alive"

#Test if there's multiple gratitudes
def test_output_when_multiple_gratitudes_added_to_the_list():
    gratitudes = Gratitudes()
    gratitudes.add("being alive")
    gratitudes.add("being healthy")
    gratitudes.add("being a maker")
    assert gratitudes.format() == "Be grateful for: being alive, being healthy, being a maker"

#Only thing I can see going wrong is if we have repeated gratitudes. Would need to adjust the code for that.