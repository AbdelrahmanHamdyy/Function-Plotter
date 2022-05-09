import numpy as np
import matplotlib.pyplot as plt
from Validation import *


class Graph:
    def __init__(self, exp, Min, Max):
        self.function = Validation.Validate(exp)
        self.minVal = Validation.IsNum(Min)
        self.maxVal = Validation.IsNum(Max)
        Validation.validateMaxMinValues(Min, Max)

    def getFunc(self, x):
        val = eval(self.function)
        return val

    def getXRange(self):
        x_list = []
        for i in range(self.minVal, self.maxVal):
            x_list.append(i)
        return x_list

    def getYRange(self):
        y_list = []
        CheckDivByZero = Validation.validateDivisionByZero(self.function, self.minVal, self.maxVal)
        for i in range(self.minVal, self.maxVal):
            if CheckDivByZero == False and i == 0:
                y_list.append(float('inf'))
            else:
                y_list.append(self.getFunc(i))
        return y_list

    def Plot(self):
        x_plot = self.getXRange()
        y_plot = self.getYRange()
        plt.plot(x_plot, y_plot, color="red", linewidth=1.5, label=self.function)
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.style.use("seaborn-dark")
        plt.grid()
        plt.show()
