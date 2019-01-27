from test_framework import generic_test
import heapq

def merge_sorted_arrays(sorted_arrays):
    # TODO - you fill in here.
    return list(heapq.merge(*sorted_arrays))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
