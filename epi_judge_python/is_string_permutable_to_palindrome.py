from test_framework import generic_test

from collections import Counter



class solution():
    def __init__(self):
        self.result = True
    def helper(self,s):
        oddflag = False
        c = Counter(s)
        for k,v in c.items():
            if (c[k] %2 == 1):
                if(oddflag ==  True):
                    self.result = False
                else:
                    oddflag = True
            
        #print(list(c.elements()))
        
        
def can_form_palindrome(s):
    # TODO - you fill in here.
    r = solution()
    r.helper(s)
    return r.result
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_string_permutable_to_palindrome.py",
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
