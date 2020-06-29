from Iris import Iris
from Histogram import Histogram


iris = Iris()
attributes = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width"]

for attr in attributes:
    print("Average " + attr + ": " + str(iris.calculate_average(attr)))
    print("Median " + attr + ": " + str(iris.calculate_median(attr)))
    print("Minimum " + attr + ": " + str(iris.get_min_range(attr)))
    print("First Quartile " + attr + ": " + str(iris.calculate_25(attr)))
    print("Third Quartile " + attr + ": " + str(iris.calculate_75(attr)))
    print("Maximum " + attr + ": " + str(iris.get_max_range(attr)))
    print("Variance " + attr + ": " + str(iris.calculate_variance(attr)) + "\n")

    histogram = Histogram(iris, attr)
    histogram.setup_data()
    histogram.build_histogram()













        






