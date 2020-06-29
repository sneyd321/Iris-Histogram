import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np


class Histogram:

    

    def __init__(self, iris, attr):
        self._iris = iris
        self._attr = attr
        self._binList = []
        self._values = []


    def setup_data(self):
        minimum = self._iris.get_min_range(self._attr)
        maximum = self._iris.get_max_range(self._attr)
        spread = maximum - minimum
        binLength = spread / 10
       
        for i in range(1, 11):
            lowerBound = round(minimum + (binLength * (i - 1)), 2)
            upperBound = round(minimum + (binLength * i), 2)
            inRange = self._iris.value_in_range(lowerBound, upperBound, self._attr)
            self._values.append(len(inRange))
            self._binList.append(str(lowerBound) + " - " + str(upperBound))


    def build_histogram(self):
        bins = tuple(self._binList)

        y_pos = np.arange(len(bins))

        plt.bar(y_pos, self._values, align='center', alpha=0.5)
        plt.xticks(y_pos, bins)
        plt.ylabel('Amount')
        plt.xlabel("Bins")
        plt.title(self._attr + ' Histogram')

        plt.show()