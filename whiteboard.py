# Given a string of letters, write a function to see if the word  (case insensitive) is a palindrome (the same word spelled forward and backwards).
# The given string will contain only letters 
# Examples:
# is_palindrome("RaceCar") \\ => True
# is_palindrome("mom")  \\ => True
# is_palindrome("Shoha") \\ => False

# Case insensitive
# only letters

# Given a case incensitive string
# We want to check if the string forward is the same as the string backwards
# Creeate a reversed copy is equal to the original string
# if it is, return True, if not return False

def solution(some_string): #always call the name of the function "solution"
    reversed_some_string = some_string[::-1]
    if reversed_some_string.lower() == some_string.lower():
        # if it is return true
        return True
    else:
        return False