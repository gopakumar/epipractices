import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook



class solution ():
    def __init__(self):
        self.result = bytearray()
    def solution(self,s):
        self.reversestring(s,0,len(s))

        
        start =0
        for i,val in enumerate(s):
            if(chr(s[i]) == " "):
                self.reversestring(s,start,i)
                start = i+1
        self.reversestring(s,start,len(s))
                
        #self.prints(s)
        
    def prints(self,s):
        for i in range (len(s)):
            print(i,s[i],chr(s[i]))
        
        
    def reversestring (self,s,start,end):
        #print(start,end)
        slen = len(s)
        for i in range(int((end-start)/2)):
           # print(i,s[i],chr(s[i]))
            index = i+start
           # print(index)
            s[index],s[end-i-1] = s[end-i-1],s[index]
        #self.prints(s)

        

# Assume s is a string encoded as bytearray.
def reverse_words(s):
    # TODO - you fill in here.
    s1 = solution()
    return s1.solution(s)
    


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = bytearray()
    s_copy.extend(map(ord, s))

    executor.run(functools.partial(reverse_words, s_copy))

    return s_copy.decode("utf-8")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_words.py", 'reverse_words.tsv',
                                       reverse_words_wrapper))
