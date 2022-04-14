def test_number(number, awesome_phrases):
    if  (number >= 100) and ((number in awesome_phrases) or #if in List
        (all(x == "0" for x in str(number)[1:])) or #Any digit followed by all zeros
        (all(x == str(number)[0] for x in str(number)[1:])) or #Every digit is the same number
        (str(number) in '1234567890') or #The digits are sequential, incementing
        (str(number) in '9876543210') or #The digits are sequential, decrementing
        (str(number) == str(number)[::-1]) #The digits are a palindrome
        ):
        return 2
    else:
        return 0

def is_interesting(number, awesome_phrases):
    if test_number(number, awesome_phrases) == 2:
        return 2
    elif test_number(number+1, awesome_phrases) == 2 or test_number(number+2, awesome_phrases) == 2:
        return 1
    else:
        return 0