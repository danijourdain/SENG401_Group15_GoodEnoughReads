import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from django.db import models
from django.db import connection, transaction
import datetime


class StatisticsModel:
    def __init__(self, email):
        self.email = email
        self.font = FontProperties()
        self.font.set_family('serif')
        self.font.set_name('Times New Roman')
        self.pages = 0
        self.cursor = connection.cursor()

    def NumPagesThisWeek(self):  
        self.cursor.execute("SELECT NewestReadingStartDate, NewestReadingEndDate, PagesRead FROM BookInUserCollection WHERE email = '" + self.email + "' ;")
        readPages = self.cursor.fetchall()

        # from: https://stackoverflow.com/questions/2003841/how-can-i-get-the-current-week-using-python#:~:text=Use%20get_week_dates(date.,to%20get%20current%20week%20dates.
        now = datetime.datetime.now()
        now_day_1 = now - datetime.timedelta(days=now.weekday())
        dates = [(now_day_1 + datetime.timedelta(days=d)).strftime("%Y-%m-%d") for d in range(7)]

        i = 0
        while i < len(readPages):
            if (str(readPages[i][1]) in dates):     # If newest reading end date is in this week add number of pages read 
                self.pages += readPages[i][2]
            i += 1

        return self.pages

    def CalculateBooksPerMonth(self):
        self.cursor.execute("SELECT NewestReadingEndDate FROM BookInUserCollection WHERE email = '" + self.email + "' ;")
        MonthlyBooksRead = self.cursor.fetchall()

        # dictionary with key value pairs: key- month, value - number of books read that month
        self.num_books_read_per_month = {"January": 0, "February": 0, "March": 0, "April": 0, "May": 0,
                                          "June": 0, "July":0, "August": 0, "September": 0, "October": 0,
                                          "November": 0, "December": 0}
        
        # get pages read of books with newest reading end date in the current month 
        # compare to total pages in that book
        # if total pages = number of pages read
        #   increase the number of books read this month 

        months = list(self.num_books_read_per_month.keys())

        i = 0
        while i < len(MonthlyBooksRead):
            current_year = datetime.date.today().year
            # print(current_year)
            # print(MonthlyBooksRead[i][0].year)
            if (MonthlyBooksRead[i][0].year == current_year):
                # print(MonthlyBooksRead[i][0].month)
                self.num_books_read_per_month[months[MonthlyBooksRead[i][0].month - 1]] += 1
            i += 1

        # print(self.num_books_read_per_month)
        return self.num_books_read_per_month



    def CalculateBooksPerYear(self):
        self.cursor.execute("SELECT NewestReadingEndDate FROM BookInUserCollection WHERE email = '" + self.email + "' ;")
        YearlyBooksRead = self.cursor.fetchall()

        # dictionary with key value pairs: key - year, value - number of books read that year 
        self.num_books_read_per_year = {"2023": 0}  # Add years as keys as searching through database
        # get pages read of books with newest reading end date in the current year
        # compare to total pages in that book
        # if total pages = number of pages read
        #   increase the number of books read this year 

        i = 0
        while i < len(YearlyBooksRead):
            if (str(YearlyBooksRead[i][0].year) in self.num_books_read_per_year):
                self.num_books_read_per_year[str(YearlyBooksRead[i][0].year)] += 1
            else:
                self.num_books_read_per_year[str(YearlyBooksRead[i][0].year)] = 1
            i += 1
        
        # print(self.num_books_read_per_year)
        return self.num_books_read_per_year

    def CalculateGenresPerYear(self): 
        self.num_genres_per_year = {}   #Add genres as keys as searching through database
        pass

    def CalculatePagesPerWeek(self):    #per 1 months, per year
        pass

    def CreateBarGraph(self, x, y, x_label, y_label, title):
        fig, ax = plt.subplots()

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        plt.bar(x, y, color = "#004643")
        plt.title(title, fontproperties = self.font, fontsize = 20)
        plt.xlabel(x_label, fontproperties = self.font, fontsize = 15)
        plt.xticks(rotation = 45, fontproperties = self.font, fontsize = 10)
        plt.ylabel(y_label, fontproperties = self.font, fontsize = 15)
        plt.yticks(fontproperties = self.font, fontsize = 10)
        
        fig.savefig('images/BarGraph' + title.replace(' ', '') + '.png')
        # plt.show()

    def CreateLineGraph(self, x, y, x_label, y_label, title):
        fig, ax = plt.subplots()

        plt.plot(x, y, color = "#004643", linewidth = 5.0, marker = 'o', markersize = 10.0, markerfacecolor = "#84A98C")
        plt.title(title, fontproperties = self.font, fontsize = 20)
        plt.xlabel(x_label, fontproperties = self.font, fontsize = 15)
        plt.xticks(rotation = 45, fontproperties = self.font, fontsize = 10)
        plt.ylabel(y_label, fontproperties = self.font, fontsize = 15)
        plt.yticks(fontproperties = self.font, fontsize = 10)

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        
        fig.savefig('images/LineGraph' + title.replace(' ', '') + '.png')
        # plt.show()

    def CreatePieChart(self, x, y, title):
        fig, ax = plt.subplots()
        PieColors = ["#84A98C"]
        PieExplode = []

        i = 0
        while i < len(x):
            if y[i] == 0:
                y.pop(i)
                x.pop(i)
            else:
                PieColors.append("#" + (str(hex(int((PieColors[i])[1:], 16) + 20)))[2:])
                PieExplode.append(0.03)
                i += 1

        plt.pie(y, labels = x, startangle = 90, colors = PieColors, pctdistance = 0.85, explode = PieExplode)
        plt.title(title, fontproperties = self.font, fontsize = 20)
        
        fig.savefig('images/PieChart' + title.replace(' ','') + '.png')

        # plt.show()

        


if __name__ == '__main__':
    books_per_month = {"January":5, "February": 7, "March": 10, "April": 10, "May": 0,
        "June": 1, "July":4, "August": 8, "September": 1, "October": 0,
        "November": 9, "December": 10}
    x = list(books_per_month.keys())
    y = list(books_per_month.values())
    x_label = "Months"
    y_label = "Number of Books read"
    title = "Number of Books read each Month"
    s = StatisticsModel("a@gmail.com")
    # s.CreateBarGraph(x, y, x_label, y_label, title)
    # s.CreatePieChart(x, y, title)
    s.NumPagesThisWeek()