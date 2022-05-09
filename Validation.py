import re
import sys


class Validation:
    def __init__(self):
        print("Validation Class")

    def Validate(Exp):
        Exp = Exp.replace(" ", "")
        if Exp == "":
            raise ValueError("Function field is empty!")
        correctFormat = "(-)?(\d+$)|((-)?(\d+[+-])?(\d+[\*\/])?[xX](\^\d+)?([+-](\d+)?([\*\/][xX](\^\d+)?)?)*)*$"
        valid = re.match(correctFormat, Exp)
        if not valid:
            raise ValueError("Invalid Function")
        Exp = Exp.replace('^', '**').replace('X', 'x')
        return Exp

    def validateMaxMinValues(Min, Max):
        if Min >= Max:
            raise ValueError("Maximum value for x must be greater than Minimum")

    def IsNum(self, val):
        if val == "":
            raise ValueError("Please Enter Max and Min values for x")
        try:
            Num = int(val)
            return Num
        except:
            raise ValueError("Max & Min values must be integer")

    def validateDivisionByZero(exp, minValue, maxValue):
        if exp.find('/X') != -1 or exp.find('/x') != -1 and minValue <= 0 and maxValue >= 0:
            return False
        return True
