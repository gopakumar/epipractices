from test_framework import generic_test

class solution ():
    def __init__ (self):
        self.result = None

    def helper(self,path):
        print (path)

def shortest_equivalent_path(path):
    # TODO - you fill in here.
    r = solution()
    r.helper(path)
    
    return ''


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("directory_path_normalization.py",
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
