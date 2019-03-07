import functools
#import pdb

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


class solution():
    def __init__(self):
        self.result = None

    def findsolution(self,node,data0,data1):
        #pdb.set_trace()
        if (node == None):
            return None
        if (node.data == data0 or node.data == data1):
            return node
        leftdata = self.findsolution(node.left,data0,data1)
        rightdata = self.findsolution(node.right,data0,data1)
        if(leftdata == None and rightdata == None):
            return None
        if(leftdata !=None and rightdata != None):
            return node
        else:
            return (leftdata or rightdata)


    def inorder(self,tree):
        if(tree):
            print(tree.data)
            self.inorder(tree.left)
            self.inorder(tree.right)
                
def lca(tree, node0, node1):
    # TODO - you fill in here.
    #pdb.set_trace()
    s= solution()
    #s.inorder(tree)
    return s.findsolution(tree,node0.data,node1.data)
    
    


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lowest_common_ancestor.py",
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
