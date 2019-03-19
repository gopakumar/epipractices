from test_framework import generic_test
import pdb
#incompleted

class solution ():
    def __init__(self):
        self.result = None

    def solution (self,prices):
        #print (prices)
        minval = prices[0]
        maxval = prices[0]
        profit = list()
        #pdb.set_trace()
        pindex = 0
        profit.append(prices[0] -minval)
        tempprofit = 0
        for x in prices:
            #        print (x,minval,maxval)
            if x < minval:
                minval = x
                profit.append(0)
                tempprofit = 0
            if x> minval:
                #print (profit)
                #profit[-1] = max(profit[-1],(x-minval))
                if ((x-minval) > profit[-1] ):
                    print(x,minval)
                    profit[-1] = x-minval

        #print (profit)
        return 0.0

     



def buy_and_sell_stock_twice(prices):
    # TODO - you fill in here.
    s = solution()
    s.solution(prices)
    return 0.0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock_twice.py",
                                       "buy_and_sell_stock_twice.tsv",
                                       buy_and_sell_stock_twice))
