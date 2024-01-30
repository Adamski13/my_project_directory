from lib.string_builder import *

#Test when initial output is an empty string
def test_initial_output_is_empty_string():
    string_builder = StringBuilder()
    assert string_builder.output() == ""

#Test when initial output is an empty string, the initial lenght of output is 0.
def test_lenght_of_initial_empty_string():
    string_builder = StringBuilder()
    assert string_builder.size() == 0
    
#Test adding a single string. Output is a single string
def test_output_adding_a_single_string():
    string_builder = StringBuilder()
    string_builder.add("Hello")
    assert string_builder.output() == "Hello"

#Test lenght of the output when input is a single string.
def test_lenght_of_the_string_when_adding_a_single_string():
    string_builder = StringBuilder()
    string_builder.add("Hello")
    assert string_builder.size() == 5
    
#Test adding multiple strings
def test_output_adding_multiple_strings():
    string_builder = StringBuilder()
    string_builder.add("Hello")
    string_builder.add(" Adam,")
    string_builder.add(" nice to meet you!")
    assert string_builder.output() == "Hello Adam, nice to meet you!"

#Test lenght of the output/concatenated string when input are multiple strings.
def test_lenght_of_output_when_adding_multiple_strings():
    string_builder = StringBuilder()
    string_builder.add("Hello")
    string_builder.add(" Adam,")
    string_builder.add(" nice to meet you!")
    assert string_builder.size() == 29
    

#Test adding integer?
    
