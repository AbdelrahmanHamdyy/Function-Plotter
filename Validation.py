import re
import sys


class Validation:
    def __init__(self):
        print("Validation Class")

    # Validate Expression
    def Validate(Exp):
        # Check for empty function field
        Exp = Exp.replace(" ", "")
        if Exp == "":
            raise ValueError("Function field is empty!")
        # Check the validity of the function format using regular expressions (regex)
        correctFormat = "(-)?(\d+$)|((-)?(\d+[+-])?(\d+[\*\/])?[xX](\^\d+)?([+-](\d+)?([\*\/][xX](\^\d+)?)?)*)*$"
        valid = re.match(correctFormat, Exp)
        if not valid:
            raise ValueError("Invalid Function")
        # Handle Power and Capital X's
        Exp = Exp.replace('^', '**').replace('X', 'x')
        return Exp

    # Maximum must be greater than Minimum
    def validateMaxMinValues(Min, Max):
        if float(Min) >= float(Max):
            raise ValueError("Maximum value for x must be greater than Minimum")

    # Check for integer input fields only
    def IsNum(n):
        if n == "":
            raise ValueError("Please Enter Max and Min values for x")
        try:
            Num = int(n)
            return Num
        except:
            raise ValueError("Max & Min values must be integer")

    # 1/x-3
    def validateDivisionByZero(exp, minValue, maxValue):
        if exp.find('/X') != -1 or exp.find('/x') != -1 and minValue <= 0 and maxValue >= 0:
            return False
        return True
