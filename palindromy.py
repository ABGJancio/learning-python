def palindrome(an_expression):
    """
        checks if a word or a phrase is a palindrome
        arguments:
            an_expression - specific word or phrase that is to be checked, (type: string) 
        returns a boolean
    """
    an_expression = an_expression.lower().replace(' ','').replace(',','').replace('.','')
    letters = an_expression[::-1]
    return print(bool(an_expression == letters))
    
palindrome('Jeż leje lwa, paw leje lżej.')