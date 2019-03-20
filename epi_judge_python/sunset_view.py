from test_framework import generic_test


class solution ():
    def __init__(self):
        self.result = []
    def helper(self,seq):
        #print(seq)
        hi = seq[-1]
        self.result.append(len(seq)-1)
        for i in range(len(seq)-2,-1,-1):
            if(seq[i]>hi):
                hi = seq[i]
                self.result.append(i)

            
def examine_buildings_with_sunset(sequence):
    # TODO - you fill in here.
    if(len(sequence) == 0):
        return sequence

    r = solution()
    r.helper(sequence)
    return r.result


def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sunset_view.py", 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
