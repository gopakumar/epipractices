from test_framework import generic_test, test_utils


def find_anagrams(dictionary):
    # TODO - you fill in here.
    list_strings = dictionary
    #print (list_strings)
    result = list()
    data_dict = dict()
    for  i,str in enumerate(list_strings):
        tkey = "".join(sorted(str))
        if tkey in data_dict:
            data_dict[tkey].append(list_strings[i])
        else:
            data_dict[tkey] = list()
            data_dict[tkey].append(list_strings[i])
    
    #print(data_dict)
    for k,v in data_dict.items():
        if len(data_dict[k]) >1:
            result.append(data_dict[k])

#    for x in result:
#        print (x)
            

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "anagrams.py",
            "anagrams.tsv",
            find_anagrams,
            comparator=test_utils.unordered_compare))
