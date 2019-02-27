from test_framework import generic_test

class solution():
    def __init__(self):
        self.result = True
    def findsolution(self,tree):
        if(tree):
            self.helper(tree.left,tree.right)
        
    def helper(self,leftnode,rightnode):

        if(leftnode == None  and rightnode == None):
            return
        elif(leftnode == None or rightnode == None):
            # if(leftnode != None):
            #     print ("left is not none",leftnode,rightnode)
            # if(rightnode != None):
            #     print ("right is not none",leftnode,rightnode)
            self.result = False
            return
        elif(leftnode.data == rightnode.data):
            self.helper(leftnode.left, rightnode.right)
            self.helper(leftnode.right, rightnode.left)
            return
        else:
            #print (leftnode.data, rightnode.data)
            self.result = False
            return 

    def inorder(self,tree):
        if(tree):
            #print(tree.data)
            self.inorder(tree.left)
            self.inorder(tree.right)


            
def is_symmetric(tree):
    # TODO - you fill in here.
    s = solution()
    s.findsolution(tree)
    #s.inorder(tree)
    return s.result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_symmetric.py",
                                       'is_tree_symmetric.tsv', is_symmetric))
