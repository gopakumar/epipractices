from test_framework import generic_test


def intersect_two_sorted_arrays(A, B):
    # TODO - you fill in here.
    #print(B)
    #print(A)
    #A = set(A)
    #A = sorted(A)
    #result = list()
    #for a in A:
    #    if a in B:
    #        result.append(a)
    # 
    #return result
    a =0;
    b=0
    result = list()
    last = None
    while (a < len(A) and b <len(B)):
        #print (A[a])
        #print (B[b])
        if (A[a] == B[b]):
            if (last != A[a]):
                result.append(A[a])
                last = A[a]
            a = a+1
            b = b+1
        elif (A[a] < B[b]):
            a = a+1
        else:
            b= b+1
        
    #print (result)
    return result



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intersect_sorted_arrays.py",
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
