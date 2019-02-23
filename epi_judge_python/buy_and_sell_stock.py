from test_framework import generic_test


def buy_and_sell_stock_once(prices):
    # TODO - you fill in here.

    #print(prices)

    minval = prices[0]
    maxval = prices[0]
    profit = prices[0] -minval
    for x in prices:
#        print (x,minval,maxval)
        if x < minval:
            minval = x
        if x> minval:
            profit = max(profit,(x-minval))
    return profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
