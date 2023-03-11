import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import MaxNLocator
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
            if (MonthlyBooksRead[i][0].year == current_year):
                self.num_books_read_per_month[months[MonthlyBooksRead[i][0].month - 1]] += 1
            i += 1

        this_month = datetime.date.today().month
        return self.num_books_read_per_month[months[this_month-1]], self.num_books_read_per_month

    def CalculateBooksPerYear(self):
        self.cursor.execute("SELECT NewestReadingEndDate FROM BookInUserCollection WHERE email = '" + self.email + "' ;")
        YearlyBooksRead = self.cursor.fetchall()

        # dictionary with key value pairs: key - year, value - number of books read that year 
        self.num_books_read_per_year = {2023: 0}  # Add years as keys as searching through database
        # get pages read of books with newest reading end date in the current year
        # compare to total pages in that book
        # if total pages = number of pages read
        #   increase the number of books read this year 

        i = 0
        while i < len(YearlyBooksRead):
            if (YearlyBooksRead[i][0].year in self.num_books_read_per_year):
                self.num_books_read_per_year[YearlyBooksRead[i][0].year] += 1
            else:
                self.num_books_read_per_year[YearlyBooksRead[i][0].year] = 1
            i += 1
        
        year_keys = list(self.num_books_read_per_year.keys())
        year_keys.sort()

        # Fill in any missing years
        # Ex. year_keys = 2020, 2022, 2023 - adds 2021
        self.sorted_num_books_read_per_year = {}
        i = 0
        while i < len(year_keys):
            if ((i + 1) < len(year_keys) and year_keys[i] + 1 != year_keys[i + 1]):
                year_keys.insert(i + 1, year_keys[i] + 1)
            if (year_keys[i] in self.num_books_read_per_year):
                self.sorted_num_books_read_per_year[year_keys[i]] = self.num_books_read_per_year[year_keys[i]]
            else:
                self.sorted_num_books_read_per_year[year_keys[i]] = 0
            i += 1


        this_year = datetime.date.today().year
        
        return self.num_books_read_per_year[this_year], self.sorted_num_books_read_per_year

    def CalculateBookPagesPerYear():
        pass

    def CalculateGenresPerYear(self): 
        self.cursor.execute("SELECT C.NewestReadingEndDate, B.Genre FROM BookInUserCollection AS C, Book AS B WHERE C.email = '" + self.email + "' AND B.ISBN = C.ISBN;")
        YearlyGenresRead = self.cursor.fetchall()

        this_year = datetime.date.today().year

        self.num_genres_per_year = {}   #Add genres as keys as searching through database

        i = 0
        while i < len(YearlyGenresRead):
            if(YearlyGenresRead[i][0].year == this_year):
                if(YearlyGenresRead[i][1] in self.num_genres_per_year):
                    self.num_genres_per_year[YearlyGenresRead[i][1]] += 1
                else:
                    self.num_genres_per_year[YearlyGenresRead[i][1]] = 1
            i += 1

        return self.num_genres_per_year

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
        
        fig.savefig('gersiteapp/static/gersiteapp/img/stats/BarGraph' + title.replace(' ', '') + '.png', bbox_inches='tight', transparent=True)

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
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))

        fig.savefig('gersiteapp/static/gersiteapp/img/stats/LineGraph' + title.replace(' ', '') + '.png', bbox_inches='tight', transparent=True)

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
        
        fig.savefig('gersiteapp/static/gersiteapp/img/stats/PieChart' + title.replace(' ','') + '.png', bbox_inches='tight', transparent=True)

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
    s.CreateBarGraph(x, y, x_label, y_label, title)
    s.CreatePieChart(x, y, title)
    # s.NumPagesThisWeek()