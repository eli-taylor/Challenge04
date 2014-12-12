## Eli's Code Challenge 4 Submission
 
#- Run script using python 3.*
#- Enter a math expression that uses valid operators +, -, /, *, (, and )

import re

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0,item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    return False

def ComparePrecedence(o1, o2): 
    if o1 == '+' and o2 == '*': # + has lower precedence than *
        return False
 
    if o1 == '*' and o2 == '-': # * has higher precedence over -
        return True

    if o1 == '+' and o2 == '/': # + has lower precedence than *
        return False
 
    if o1 == '/' and o2 == '-': # * has higher precedence over -
        return True
 
    if o1 == '+' and o2 == '-': # + has same precedence over -
        return True
 
    return True

def AddMultiplicationSymbol(expArr):
    indexArr = list()
    try:
        index = expArr.index('(')
    except:
        index = -1
    
    while index >= 0:
        if index > 0:
            if expArr[index - 1] == ')' or is_number(expArr[index - 1]):
                expArr.insert(index, '*')
                index += 1

        try:
            index = expArr.index('(', index + 1)
        except:
            index = -1

    return expArr

def ApplyOperator(op1, op2, optr):
    if optr == '+':
        return float(op2) + float(op1);
    if optr == '-':
        return float(op2) - float(op1);
    if optr == '*':
        return float(op2) * float(op1);
    if optr == '/':
        return float(op2) / float(op1);
        
    return -1;

def GetExpressionArray(mystr):
    #remove if any spaces from the expression
    mystr = mystr.replace("\\s+", "")
    
    stack = Stack()
    #we assume that the expression is in valid format
    pattern = re.compile(u'(\\b\\w*[\\.]?\\w+\\b|[\\(\\)\\+\\*\\-\\/])') 
    expArr = re.findall(pattern, mystr)

    expArr = AddMultiplicationSymbol(expArr)

    return expArr

def ConvertToPostfix(infix):
    length = len(infix)
    stack = Stack()
    postfix = list()
    
    for val in infix:
        if is_number(val):
            postfix.append(val)# = postfix + (str(token))
        elif val == '(':
            stack.push(val)
        elif val == '*' or val == '+' or val == '-' or val == '/':
            while stack.size() > 0 and stack.peek() != '(':
                if ComparePrecedence(stack.peek(), val):
                    postfix.append(stack.pop())
                else:
                    break

            stack.push(val)
        elif val == ')':
            while stack.size() > 0 and stack.peek() != '(':
                postfix.append(stack.pop())

            if stack.size() > 0:
                stack.pop()

    while stack.size() > 0:
        postfix.append(stack.pop())
    
    return postfix

def EvaluatePostfix(postfix):
    resultStack = Stack()
    length = len(postfix)
    
    if length == 0:
        return 'ERROR: Invalid format'

    try:
        for val in postfix:
            if val == '*' or val == '+' or val == '-' or val == '/':
                result = ApplyOperator(resultStack.pop(), resultStack.pop(), val)
                resultStack.push(result)
            elif is_number(val):
                resultStack.push(val)
    except:
        return 'ERROR: Invalid format'

    return resultStack.pop()

userInput = ''
while userInput == '':
   userInput = input('Enter an expression to evaluate: ')

while userInput != 'q' and userInput != 'x':
    infixArray = GetExpressionArray(userInput)
    postfixArray = ConvertToPostfix(infixArray)
    answer = EvaluatePostfix(postfixArray)
    print(answer)
    
    userInput = ''
    while userInput == '':
        userInput = input("Enter an expression to evaluate ('q' or 'x' to exit): ")
