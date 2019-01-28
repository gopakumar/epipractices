from test_framework import generic_test
import heapq

def merge_sorted_arrays(sorted_arrays):
    # TODO - you fill in here.
    #return list(heapq.merge(*sorted_arrays))
#    print (sorted_arrays)
    pointer_array = [iter(x) for x in sorted_arrays]
    min_heap = list()
    for i, arr in enumerate(pointer_array):
        first = next(arr,None)
        #print(first)
        if first is  not None :
            heapq.heappush(min_heap,(first,i))

    result = []
    while min_heap:
        minvalue= heapq.heappop(min_heap)
        #print (minvalue[0],minvalue[1])
        i = minvalue[1]
        result.append(minvalue[0])
        first = next(pointer_array[i],None)
        #print(first)
        if first is  not None :
            heapq.heappush(min_heap,(first,i))
            #print (min_heap)
    return result
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
