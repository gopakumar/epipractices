
from test_framework import generic_test
from list_node import ListNode

def reverse_sublist(L, start, finish):

    head = temp_head = ListNode(0,L)
    for _ in range(1,start):
        temp_head = temp_head.next
       
    last_node = temp_head.next
    for _ in range (finish-start):
     

        temp = last_node.next
        last_node.next = temp.next
        temp.next = temp_head.next
        temp_head.next = temp
        
    return head.next

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_sublist.py",
                                       "reverse_sublist.tsv", reverse_sublist))
