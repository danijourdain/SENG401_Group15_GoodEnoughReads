import numpy as np
import matplotlib.pyplot as plt
import django

class StatisticsModel:
    def __init__(self, email):
        self.email = email

    def CalculateBooksPerMonth(self):
        # dictionary with key value pairs: key- month, value - number of books read that month
        self.num_books_read_per_month = {"January":0, "February": 0, "March": 0, "April": 0, "May": 0,
                                          "June": 0, "July":0, "August": 0, "September": 0, "October": 0,
                                          "November": 0, "December": 0}
        # get pages read of books with newest reading end date in the current month 
        # compare to total pages in that book
        # if total pages = number of pages read
        #   increase the number of books read this month 
        pass 

    def CalculateBooksPerYear(self):
        # dictionary with key value pairs: key - year, value - number of books read that year 
        self.num_books_read_per_year = {"2023": 0}  # Add years as keys as searching through database
        # get pages read of books with newest reading end date in the current year
        # compare to total pages in that book
        # if total pages = number of pages read
        #   increase the number of books read this year 
        pass

    def CalculateGenresPerYear(self): 
        self.num_genres_per_year = {}   #Add genres as keys as searching through database
        pass

    def CalculatePagesPerWeek(self):    #per 1 months, per year
        pass

    def CreateBarGraph(self, x, y, x_label, y_label, title):
        plt.bar(x, y)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()

    def CreateLineGraph(self, x, y):
        pass

    def CreatePieChart(self):
        pass


if __name__ == '__main__':
    books_per_month = {"January":5, "February": 7, "March": 10, "April": 10, "May": 0,
        "June": 1, "July":4, "August": 8, "September": 1, "October": 0,
        "November": 9, "December": 10}
    x = books_per_month.keys()
    y = books_per_month.values()
    x_label = "Months"
    y_label = "Number of Books read"
    title = "Number of Books read each Month"
    s = StatisticsModel("email")
    s.CreateBarGraph(x, y, x_label, y_label, title)