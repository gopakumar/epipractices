from test_framework import generic_test


class solution ():
    def __init__ (self):
        self.result = None

    def helper(self,s):
        print (s)

        
def is_well_formed(s):
    # TODO - you fill in here.
    r = solution()
    r.helper(s)
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_parenthesization.py",
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
