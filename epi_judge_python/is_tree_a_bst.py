from test_framework import generic_test

#flag = True

def is_binary_tree_bst(tree, low_range=float('-inf'), high_range=float('inf')):
    # TODO - you fill in here.
    global flag
    flag = True

    def helper(tree,is_left):
        global flag
        if (tree and flag):
            if ((tree.left) and (tree.left.data > tree.data)):
                flag = False
                return None
            if ((tree.right) and (tree.right.data < tree.data)):
                flag = False
                return None
            leftmax = helper(tree.left,True)

            rightmin = helper(tree.right,False)

            if (leftmax is not None) and (leftmax > tree.data):
                flag = False
                return None
            if (rightmin is not None) and (rightmin < tree.data):
                flag = False
                return None

            leftmax = leftmax if leftmax is not None  else tree.data
            rightmin = rightmin if rightmin is not None  else tree.data
            print ("max , min ",leftmax,rightmin,tree.data)

            if (is_left is None):
                if (leftmax > tree.data or rightmin < tree.data):
                    flag = False
                    return 
            
            if (is_left is True ):
                return max(leftmax,rightmin,tree.data)
            else:
                return min(leftmax,rightmin,tree.data)
        else:
            return None

    helper(tree, None)
    return flag



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_a_bst.py", 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
