import functools
import pdb
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

class solution():
    def __init__(self):
        self.result= None
        self.count = 0
    def helper(self,node,k):
        #pdb.set_trace()
        if(node):
            self.helper(node.left,k)
            self.count = self.count+1
            if(self.count == k):
                self.result = node
            self.helper(node.right,k)
    def helperk(self,node,k):
        #pdb.set_trace()
        if(node):
            if((self.count+node.size) < k):
                self.count = self.count+node.size
            else:
                self.helperk(node.left,k)
                self.count = self.count+1
                if(self.count == k):
                    self.result = node
                self.helperk(node.right,k)
        
            
                
            
    
class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None, size=None):
        self.data = data
        self.left = left
        self.right = right
        self.size = size


def find_kth_node_binary_tree(tree, k):
    
    # TODO - you fill in here.
    r = solution()
    #r.helper(tree,k)
    r.helperk(tree,k)
    return r.result


@enable_executor_hook
def find_kth_node_binary_tree_wrapper(executor, tree, k):
    def init_size(node):
        if not node:
            return 0
        node.size = 1 + init_size(node.left) + init_size(node.right)
        return node.size

    init_size(tree)

    result = executor.run(
        functools.partial(find_kth_node_binary_tree, tree, k))

    if not result:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("kth_node_in_tree.py",
                                       "kth_node_in_tree.tsv",
                                       find_kth_node_binary_tree_wrapper))
