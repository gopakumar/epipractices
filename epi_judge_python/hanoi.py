import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

NUM_PEGS = 3

result = list()
def compute_tower_hanoi(num_rings):
    # TODO - you fill in here.
    #print("\n")
    global result
    result = list()
    #print (result)
    if(1 == num_rings):
        result.append([0,1])
    else:
        source =0
        dest=1
        temp = 2
        n= num_rings
        helper(source,dest,temp,num_rings)
        
    #print (result)
    return result

def helper(source,dest,temp,n):
    global result
    if (n >  2):
        helper(source,temp,dest,n-1)
        result.append([source,dest])
        helper(temp,dest,source,n-1)
    elif(n==2):
        result.append([source,temp])
        result.append([source,dest])
        result.append([temp,dest])
    #print(result)



@enable_executor_hook
def compute_tower_hanoi_wrapper(executor, num_rings):
    pegs = [list(reversed(range(1, num_rings + 1)))] + [[] for _ in range(
        1, NUM_PEGS)]

    result = executor.run(functools.partial(compute_tower_hanoi, num_rings))

    for from_peg, to_peg in result:
        if pegs[to_peg] and pegs[from_peg][-1] >= pegs[to_peg][-1]:
            raise TestFailure("Illegal move from {} to {}".format(
                pegs[from_peg][-1], pegs[to_peg][-1]))
        pegs[to_peg].append(pegs[from_peg].pop())
    expected_pegs1 = [[], [], list(reversed(range(1, num_rings + 1)))]
    expected_pegs2 = [[], list(reversed(range(1, num_rings + 1))), []]
    if pegs not in (expected_pegs1, expected_pegs2):
        raise TestFailure("Pegs doesn't place in the right configuration")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("hanoi.py", 'hanoi.tsv',
                                       compute_tower_hanoi_wrapper))
