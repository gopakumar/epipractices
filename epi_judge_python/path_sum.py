from test_framework import generic_test

class solution():
    def __init__(self):
        self.result = False
        self.sum = 0
    def helper(self,node,val):
        val = val+node.data
        if(node.left == None and node.right == None):
            if (val== self.sum):
                self.result = True
        else:
            if(node.left):
                self.helper(node.left,val)
            if(node.right):
                self.helper(node.right,val)
        
        
def has_path_sum(tree,remaining_weight):
    # TODO - you fill in here.
    r = solution()
    r.sum = remaining_weight
    if(tree):
        r.helper(tree,0)
    return r.result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("path_sum.py", 'path_sum.tsv',
                                       has_path_sum))
