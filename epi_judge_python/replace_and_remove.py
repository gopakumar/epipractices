import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size, s):
    #print (size,s)
    i = size-1
    ri = len(s)-1
    while (i>=0):
        #print (s[i])
        if (s[i] == 'b'):
            i = i-1
        elif (s[i]== 'a'):
            s[ri] = 'd'
            ri= ri-1
            s[ri] = 'd'
            ri= ri-1
            i=i-1
        elif(s[i] == 'c'):
            s[ri] = 'c'
            ri= ri-1
            i=i-1
        elif(s[i] == 'd'):
            s[ri] = 'd'
            ri= ri-1
            i=i-1
        else:
            i=i-1
    # TODO - you fill in here.
    result = s[ri+1::]
    s = result
    #print(s[ri+1::])
    print (result)
    print(s)
    return len(result)


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("replace_and_remove.py",
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
