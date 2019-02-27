from test_framework import generic_test
from binary_tree_node import BinaryTreeNode

class solution():
    def __init__(self):
        self.result = True

    def inorder(self,node):
        if(node):
            #print(node.data)
            hleft = self.inorder(node.left)
            hright = self.inorder(node.right)
            if (abs(hleft-hright) > 1):
                self.result = False
                return 0
            else:
                return max(hleft,hright)+1
        else:
            return 0 

def is_balanced_binary_tree(tree):
    # TODO - you fill in here
    s = solution()
    s.inorder(tree)
    return s.result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
