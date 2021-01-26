def palindrome(an_expression):
    """
        checks if a word or a sentence is a palindrome
        arguments:
            an_expression
        Returns a Boolean
    """
    an_expression = an_expression.lower() # na wypadek wpisania wielkich liter
    an_expression = an_expression.replace(' ','') # na wypadek wpisania wyrażenia
    letters = [l for l in an_expression]
    letters.reverse()
    letters = ''.join(letters)
    return print(bool(an_expression == letters))
    
# help(palindrome)
palindrome('Jeż leje lwa paw leje lżej')