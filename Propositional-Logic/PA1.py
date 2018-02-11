######## Do not modify the following block of code ########
# ********************** BEGIN *******************************

from functools import partial
import re


class Infix(object):
    def __init__(self, func):
        self.func = func
    def __or__(self, other):
        return self.func(other)
    def __ror__(self, other):
        return Infix(partial(self.func, other))
    def __call__(self, v1, v2):
        return self.func(v1, v2)

@Infix
def implies(p, q) :
    return not p or q

@Infix
def iff(p, q) :
    return (p |implies| q) and (q |implies| p)


# You must use this function to extract variables
# This function takes an expression as input and returns a sorted list of variables
# Do NOT modify this function
def extract_variables(expression):
    sorted_variable_set = sorted(set(re.findall(r'\b[a-z]\b', expression)))
    return sorted_variable_set

# *********************** END ***************************


# This function calculates a truth table for a given expression
# input: expression
# output: truth table as a list of lists
# You must use extract_variables function to generate the list of variables from expression
# return a list of lists for this function
def truth_table(expression):
    resultarray = []
    finalarray = []
    array = extract_variables(expression)
    recursive_method(resultarray, finalarray, len(array))

    for i in resultarray:
        for j in range(len(array)):
            exec(array[j] + '=' + str(i[j]))
        i.append(eval(expression))

    return resultarray
    pass

def recursive_method(resultarray, finalarray, length):
    if(length == 1):
        resultarray.append(finalarray + [True])
        resultarray.append(finalarray + [False])
    else:
        recursive_method(resultarray, finalarray + [True], length - 1)
        recursive_method(resultarray, finalarray + [False], length - 1)


# count the number of satisfying values
# input: expression
# output: number of satisfying values in the expression
def count_satisfying(expression):
    truth1 = truth_table(expression)
    count = 0
    for i in truth1:
        if i[len(i) - 1] == True:
            count = count+1
    return count

# if the expression is a tautology return True,
# False otherwise
# input: expression
# output: bool
def is_tautology(expression):
    truth1 = truth_table(expression)
    number = count_satisfying(expression)
    if(number == len(truth1) == True):
        return True
    else:
        return False
    pass

# if expr1 is equivalent to expr2 return True,
# False otherwise
# input: expression 1 and expression 2
# output: bool
def are_equivalent(expr1, expr2):
    truth1 = truth_table(expr1)
    truth2 = truth_table(expr2)
    extract1 = extract_variables(expr1)
    extract2 = extract_variables(expr2)

    if truth1 != truth2:
        return False
    if extract1 != extract2:
        return False
    return True
