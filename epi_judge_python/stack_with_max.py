from test_framework import generic_test
from test_framework.test_failure import TestFailure
from collections import namedtuple


class Stack:

    SE = namedtuple("SE",("element","max"))
    def __init__(self):
        self.data =list()
    def empty(self):
        # TODO - you fill in here.
        
        return (len(self.data)) ==0

    def max(self):
        # TODO - you fill in here.
        if self.empty():
            raise IndexError('max(): empty stack')
        return self.data[-1].max

    def pop(self):
        # TODO - you fill in here.
        if self.empty():
            raise IndexError('pop(): empty stack')
        return self.data.pop().element

    def push(self, x):
        # TODO - you fill in here.
        self.data.append(self.SE(x,x if self.empty() else max(x,self.max())))
        return


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure(
                        "Pop: expected " + str(arg) + ", got " + str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure(
                        "Empty: expected " + str(arg) + ", got " + str(result))
            else:
                raise RuntimeError("Unsupported stack operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("stack_with_max.py",
                                       'stack_with_max.tsv', stack_tester))
