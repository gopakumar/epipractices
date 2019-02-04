from test_framework import generic_test


def intersect_two_sorted_arrays(A, B):
    # TODO - you fill in here.
    #print(B)
    #print(A)
    A = set(A)
    A = sorted(A)
    result = list()
    for a in A:
        if a in B:
            result.append(a)
    
    return result



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intersect_sorted_arrays.py",
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
