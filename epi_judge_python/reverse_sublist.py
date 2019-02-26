
from test_framework import generic_test
from list_node import ListNode

def reverse_sublist(L, start, finish):

    temp = head =  ListNode(0,L)
    count =1
    if (start == 0):
        return L
    
    while (head != None):
        if(start == count):
            break
        count = count+1
        head = head.next
    #head is the starting node
    endnode = head.next

    while(start != finish):
        
        firstlink = head.next
        lastlink = endnode.next.next
        #print(firstlink.data)
        #print(endnode.next.data)
        #print(lastlink.data)
        head.next = endnode.next
        head.next.next = firstlink
        endnode.next = lastlink
        start = start+1

    return temp.next

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_sublist.py",
                                       "reverse_sublist.tsv", reverse_sublist))
