from test_framework import generic_test


def is_palindrome(s):
    # TODO - you fill in here.
    l =  len(s)
    s = s.lower()

    #print(s)
    si = 0
    ei = len(s)-1
    if(len(s) == 0):
        return True
    while (si <= ei):
        if (s[si].isalnum() == False):
            si= si+1
        elif(s[ei].isalnum() == False):
            ei= ei-1
        elif(s[si] != s[ei]):
            return False
        else:
            si= si+1
            ei= ei-1
            
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_string_palindromic_punctuation.py",
                                       "is_string_palindromic_punctuation.tsv",
                                       is_palindrome))
