from test_framework import generic_test
from collections import deque
class solution():
    def __init__ (self):
        self.result = list()
    def helper(self,q):
        tempval = []

        while (len(q)>0):
            for x in range(len(q)):
                node = q.popleft()
                tempval.append(node.data)
                if(node.left):
                    q.append(node.left)
                if(node.right):
                    q.append(node.right)
            self.result.append(tempval)
            tempval = []
        #print(self.result)
           
        

    def inorder(self,tree):
        if(tree == None):
            return
        else:
            self.inorder(tree.left)
            #print(tree.data)
            self.inorder(tree.right)
    def getval(self,A):
        temp = []
        for x in range(len(A)):
            if(A[i] != None):
                temp.append(A[i].data)
        return temp
                
        
def binary_tree_depth_order(tree):
    # TODO - you fill in here.
    r = solution()
    q = deque()
    if(tree == None):
        return []
    q.append(tree)
    r.helper(q)
    #r.inorder(tree)

    return r.result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_level_order.py",
                                       "tree_level_order.tsv",
                                       binary_tree_depth_order))
