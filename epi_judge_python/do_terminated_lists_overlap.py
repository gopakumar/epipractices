import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook



class solution ():
    def __init__(self):
        self.result = None
    def helper(self,l0,l1):
        len1 = self.findlength(l0)
        len2 = self.findlength(l1)
        #print (len1,len2)

        diff = abs (len1-len2)
        tlist = l1
        if(len1 > len2):
            for x in range(diff):
                l0 = l0.next
        else:
            for x in range (diff):
                l1 = l1.next

        for x in range(min(len1,len2)):

            if(l0 == None or l1 == None):
                return None
            else:
                #print (l0.data,l1.data)
                if(l0 == l1):
                    return l0
                else:
                    l0 = l0.next
                    l1 = l1.next
                    
                
            
                    


    def findlength(self,l):
        length = 0
        while l:
            length = length+1
            l= l.next
        return length
    
def overlapping_no_cycle_lists(l0, l1):
    # TODO - you fill in here.
    s = solution()
    return s.helper(l0,l1)
    
    #return None


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(
        functools.partial(overlapping_no_cycle_lists, l0, l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("do_terminated_lists_overlap.py",
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
