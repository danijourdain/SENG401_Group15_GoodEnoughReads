import numpy 
import matplotlib
import django

class StatisticsModel:
    def __init__(self, d, p, b):
        self.date = d
        self.pages = p
        self.book = b

    def CalculateBooksPerMonth(self):
        pass

    def CalculateBooksPerYear(self):
        pass

    def CalculateGenresPerYear(self):
        pass

    def CalculatePagesPerWeek(self):
        pass

    def CreateBarGraph(self):
        pass

    def CreateLineGraph(self):
        pass

    def CreatePieChart(self):
        pass


