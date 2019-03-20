from test_framework import generic_test

class solution():
    def __init__(self):
        self.result = []
    def helper(self,tree):
        stack = []
        current = tree
        done =0
        while(not done):
            if(current ):
                stack.append(current)
                current = current.left
            else:
                if(len(stack)>0):
                    current = stack.pop()
                    self.result.append(current.data)
                    current = current.right
                else:
                    done = 1
        
    
    
        
def inorder_traversal(tree):
    # TODO - you fill in here.
    r = solution()
    r.helper(tree)
    
    return r.result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_inorder.py", 'tree_inorder.tsv',
                                       inorder_traversal))
