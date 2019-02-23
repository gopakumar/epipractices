from test_framework import generic_test


def ss_decode_col_id(col):
    # TODO - you fill in here.
    print (col)
    col.lstrip()
    col =col.lower()
    l = len(col)
    charlist = list(col)
    result =0
    for x in charlist:
        result = result + (26**(l-1)*(ord(x)-ord('a')+1))
        l = l-1
    return result



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spreadsheet_encoding.py",
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
