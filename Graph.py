import numpy as np
import matplotlib.pyplot as plt
from Validation import *


class Graph:
    def __init__(self, exp, Min, Max):
        # Validate all the input (Expression & Limits)
        self.function = Validation.Validate(exp)
        self.minVal = Validation.IsNum(Min)
        self.maxVal = Validation.IsNum(Max)
        Validation.validateMaxMinValues(Min, Max)

    # Evaluate the expression with x
    def getFunc(self, x):
        val = eval(self.function)
        return val

    # Range of x values
    def getXRange(self):
        x_list = []
        for i in range(self.minVal, self.maxVal):
            x_list.append(i)
        return x_list

    # Append Function output to list of y values for plotting
    def getYRange(self):
        y_list = []
        # Check for division by zero to be replaced with an asymptote on the graph
        CheckDivByZero = Validation.validateDivisionByZero(self.function, self.minVal, self.maxVal)
        for i in range(self.minVal, self.maxVal):
            if not CheckDivByZero and i == 0:
                # 1/0 = INFINITY
                y_list.append(float('inf'))
            else:
                y_list.append(self.getFunc(i))
        return y_list

    def Plot(self):
        # Get Limits
        x_plot = self.getXRange()
        y_plot = self.getYRange()
        # Plot
        plt.plot(x_plot, y_plot, color="red", linewidth=1.5, label=self.function)
        # Set Labels
        plt.xlabel("X")
        plt.ylabel("Y")
        # Style
        plt.style.use("seaborn-dark")
        # Grid & Show
        plt.grid()
        plt.show()
