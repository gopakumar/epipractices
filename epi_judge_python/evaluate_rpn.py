from test_framework import generic_test


def evaluate(expression):
    # TODO - you fill in here.
        #print(type(expression))
        
        listexpr  = expression.split(",")
        #print (listexpr)
        #print(int(listexpr[3]))
        stack = list()

        for i, item in enumerate(listexpr):

            if (len(item)>1):
                stack.append(int(item))
            elif(item.isnumeric()):
                stack.append(int(item))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                if(item == '+'):
                    stack.append(op1+op2)
                elif(item == '-'):
                    stack.append(op1-op2)
                elif(item == '*' or item == 'x' or item == 'X'):
                    stack.append(op1*op2)
                elif(item == '/'):
                    stack.append(int(op1/op2))
        return stack.pop()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("evaluate_rpn.py", 'evaluate_rpn.tsv',
                                       evaluate))
