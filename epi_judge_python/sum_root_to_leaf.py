from test_framework import generic_test

class solution ():
    def __init__ (self):
        self.result = 0

    def helper(self,node,val):
        val = val*2+node.data
        if (node.left == None and node.right == None):
            self.result = self.result + val
        else:
            
            if(node.left):
                self.helper(node.left,val)
            if(node.right):
                self.helper(node.right,val)
            
    
        
        
def sum_root_to_leaf(tree, partial_path_sum=0):
    # TODO - you fill in here.

    r = solution ()
    if(tree):
        r.helper(tree,0)
    return r.result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "sum_root_to_leaf.py", 'sum_root_to_leaf.tsv', sum_root_to_leaf))
