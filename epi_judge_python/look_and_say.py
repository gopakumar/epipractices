from test_framework import generic_test
import pdb

class solution():
    def __init__(self):
        self.result = None
    def findsolution(self,n):
        #pdb.set_trace()
        #print (n)
        out = ['1']
        temp = list()
        for x in rnn out = temp
            temp = []
        #print (out)
        self.result = "".join(out)

        
def look_and_say(n):
    # TODO - you fill in here.
    s = solution()
    if (n <= 0):
        return None
    if (n ==1):
        return "1"
    s.findsolution(n-1)
    return s.result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("look_and_say.py", "look_and_say.tsv",
                                       look_and_say))
