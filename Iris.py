import pandas as pd
import math
from Record import Record

class Iris:

    def __init__(self):
        columns = ["SepalLength", "SepalWidth", "PedalLength", "PedalWidth", "Classification"]
        self._data = pd.read_csv("iris.csv", names=columns)
        self._records = self.getRecordList()

    def getRecordList(self):
        records = []
        for index, row in self._data.iterrows():
            record = Record(row.SepalLength, row.SepalWidth, row.PedalLength, row.PedalWidth, row.Classification)
            records.append(record)
        return records

    def calculate_average(self, attr):
        total = 0
        for record in self._records:
            if attr == "Sepal Length":
                total += record.getSepalLength()
            elif attr == "Sepal Width":
                total += record.getSepalWidth()
            elif attr == "Petal Length":
                total += record.getPedalLength()
            elif attr == "Petal Width":
                total += record.getPedalWidth()
            else:
                print("Invalid Attribute Name")
                return 0
        return round(total/len(self._records), 2)
    

    def calculate_median(self, attr):
        listToBeSorted = []
        for record in self._records:
            if attr == "Sepal Length":
                value = record.getSepalLength()
                listToBeSorted.append(value)
            elif attr == "Sepal Width":
                value = record.getSepalWidth()
                listToBeSorted.append(value)
            elif attr == "Petal Length":
                value = record.getPedalLength()
                listToBeSorted.append(value)
            elif attr == "Petal Width":
                value = record.getPedalWidth()
                listToBeSorted.append(value)
            else:
                print("Invalid Attribute Name")
                return 0
        listToBeSorted.sort()
        size = len(listToBeSorted)
        
        position = int(size/2) + 1
        return listToBeSorted[int(position)]
      

        


    def calculate_25(self, attr):
        listToBeSorted = []
        for record in self._records:
            if attr == "Sepal Length":
                value = record.getSepalLength()
                listToBeSorted.append(value)
            elif attr == "Sepal Width":
                value = record.getSepalWidth()
                listToBeSorted.append(value)
            elif attr == "Petal Length":
                value = record.getPedalLength()
                listToBeSorted.append(value)
            elif attr == "Petal Width":
                value = record.getPedalWidth()
                listToBeSorted.append(value)
            else:
                print("Invalid Attribute Name")
                return 0
                
        listToBeSorted.sort()
        
        size = len(listToBeSorted)
   
        position = int(size/4) + 1
        return listToBeSorted[int(position)]
            

       


    def calculate_75(self, attr):
        listToBeSorted = []
        for record in self._records:
            if attr == "Sepal Length":
                value = record.getSepalLength()
                listToBeSorted.append(value)
            elif attr == "Sepal Width":
                value = record.getSepalWidth()
                listToBeSorted.append(value)
            elif attr == "Petal Length":
                value = record.getPedalLength()
                listToBeSorted.append(value)
            elif attr == "Petal Width":
                value = record.getPedalWidth()
                listToBeSorted.append(value)
            else:
                print("Invalid Attribute Name")
                return 0
                
        listToBeSorted.sort()
        
        size = len(listToBeSorted)
       
        position = int((size/4)) * 3 + 1
        return listToBeSorted[int(position)]

       
        


    def calculate_variance(self, attr):
        average = self.calculate_average(attr)
        squaredValues = []
        for record in self._records:
            if attr == "Sepal Length":
                value = record.getSepalLength() - average
                squaredValue = value ** 2
                squaredValues.append(squaredValue)
            elif attr == "Sepal Width":
                value = record.getSepalWidth() - average
                squaredValue = value ** 2
                squaredValues.append(squaredValue)
            elif attr == "Petal Length":
                value = record.getPedalLength() - average
                squaredValue = value ** 2
                squaredValues.append(squaredValue)
            elif attr == "Petal Width":
                value = record.getPedalWidth() - average
                squaredValue = value ** 2
                squaredValues.append(squaredValue)
            else:
                print("Invalid Attribute Name")
                return 0
                
        variance = 0
        for squaredValue in squaredValues:
            variance += squaredValue

        return round(variance/(len(squaredValues) - 1), 2) 
    
    def get_max_range(self, attr):
        filteredList = []
        for record in self._records:
            if attr == "Sepal Length":
                filteredList.append(record.getSepalLength())
            elif attr == "Sepal Width":
                filteredList.append(record.getSepalWidth())
            elif attr == "Petal Length":
                filteredList.append(record.getPedalLength())
            elif attr == "Petal Width":
                filteredList.append(record.getPedalWidth())
            else:
                print("Invalid Attribute Name")
                return 0

        
        return max(filteredList)

    def get_min_range(self, attr):
        filteredList = []
        for record in self._records:
            if attr == "Sepal Length":
                filteredList.append(record.getSepalLength())
            elif attr == "Sepal Width":
                filteredList.append(record.getSepalWidth())
            elif attr == "Petal Length":
                filteredList.append(record.getPedalLength())
            elif attr == "Petal Width":
                filteredList.append(record.getPedalWidth())
            else:
                print("Invalid Attribute Name")
                return 0

        return min(filteredList)

    def value_in_range(self, lower, upper, attr): 
        inRange = []
   
        for record in self._records: 
            if attr == "Sepal Length":
                if record.getSepalLength() >= lower and record.getSepalLength() <= upper: 
                    inRange.append(record.getSepalLength())

            elif attr == "Sepal Width":
                if record.getSepalWidth() >= lower and record.getSepalWidth() <= upper: 
                    inRange.append(record.getSepalWidth())

            elif attr == "Petal Length":
                if record.getPedalLength() >= lower and record.getPedalLength() <= upper: 
                    inRange.append(record.getPedalLength())

            elif attr == "Petal Width":
                if record.getPedalWidth() >= lower and record.getPedalWidth() <= upper: 
                    inRange.append(record.getPedalWidth())

            else:
                print("Invalid Attribute Name")
                return 0
        
        return inRange