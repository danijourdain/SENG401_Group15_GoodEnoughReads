import matplotlib
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import MaxNLocator
from django.db import models
from django.db import connection, transaction
import datetime
import plotly as py
import plotly.express as px
from pandas import DataFrame

matplotlib.use('SVG')

class StatisticsModel:
    def __init__(self, email):
        self.email = email
        self.font = FontProperties()
        self.font.set_family('serif')
        self.font.set_name('Times New Roman')
        self.pages = 0
        self.cursor = connection.cursor()

    def NumPagesThisWeek(self):  
        self.cursor.execute("SELECT NewestReadingStartDate, NewestReadingEndDate, PagesRead FROM BookInUserCollection WHERE email = %s;", [self.email])
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

    def NumPages(self):
        self.cursor.execute("SELECT PagesRead FROM BookInUserCollection WHERE email = %s;", [self.email])
        readPages = self.cursor.fetchall()
        totalReadPages = 0

        i = 0
        while i < len(readPages):
            totalReadPages += readPages[i][0]
            i+= 1

        return totalReadPages

    def CalculateBooksPerMonth(self):
        # query to get newest reading end date for every book in the users collection - each book will have only oneneweest reading end date
        self.cursor.execute("SELECT NewestReadingEndDate FROM BookInUserCollection WHERE email = %s;", [self.email])
        MonthlyBooksRead = self.cursor.fetchall()

        # dictionary with key value pairs: key- month, value - number of books read that month
        self.num_books_read_per_month = {"January": 0, "February": 0, "March": 0, "April": 0, "May": 0,
                                          "June": 0, "July":0, "August": 0, "September": 0, "October": 0,
                                          "November": 0, "December": 0}
    
        # If the newest reading end date is in this year
        #   increase the number of books read that month 

        months = list(self.num_books_read_per_month.keys())

        i = 0
        while i < len(MonthlyBooksRead):
            current_year = datetime.date.today().year
            if (MonthlyBooksRead[i][0] == None):
                print()
            elif (MonthlyBooksRead[i][0].year == current_year):
                self.num_books_read_per_month[months[MonthlyBooksRead[i][0].month - 1]] += 1
            i += 1

        this_month = datetime.date.today().month

        # return books read this month and books read every month this year
        return self.num_books_read_per_month[months[this_month-1]], self.num_books_read_per_month

    def CalculateBooksPerYear(self):
        # query to get newest reading end date for every book in the users collection - each book will have only oneneweest reading end date
        self.cursor.execute("SELECT NewestReadingEndDate FROM BookInUserCollection WHERE email = %s;", [self.email])
        YearlyBooksRead = self.cursor.fetchall()

        # dictionary with key value pairs: key - year, value - number of books read that year 
        self.num_books_read_per_year = {2023: 0}  # Add years as keys as searching through database
        # get pages read of books with newest reading end date in the current year
        # if the date is not none
        #   if the year already exists in the dictionary, increase the key for that year by one 
        #   elif the year is not a key, add it as a key and set it to one

        i = 0
        while i < len(YearlyBooksRead):
            if (YearlyBooksRead[i][0] == None):
                print()
            elif (YearlyBooksRead[i][0].year in self.num_books_read_per_year):
                self.num_books_read_per_year[YearlyBooksRead[i][0].year] += 1
            else:
                self.num_books_read_per_year[YearlyBooksRead[i][0].year] = 1
            i += 1
        
        year_keys = list(self.num_books_read_per_year.keys())
        year_keys.sort()

        # Fill in any missing years
        # Ex. year_keys = 2020, 2022, 2023 - adds 2021 key with value 0 
        # This creates a more accurate graph
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
        
        # return books read this year and number of books read every year 
        return self.num_books_read_per_year[this_year], self.sorted_num_books_read_per_year

    def CalculateBookPagesPerYear(self):
        # query to get newest reading end date and number of pages in the book for each book in the users collection - each book will have only oneneweest reading end date
        self.cursor.execute("SELECT C.NewestReadingEndDate, B.Pages FROM BookInUserCollection AS C, Book AS B WHERE C.email = %s AND B.APIid = C.ISBN;", [self.email])
        YearlyBooksPagesRead = self.cursor.fetchall()

        this_year = datetime.date.today().year

        # dictionary with key value pairs - key is the number of pages in the book, value is number of books of that length read this year
        self.book_pages_year = {"< 100": 0, "100-200": 0, "200-400": 0, "400-600": 0, "> 600": 0}

        # if date is not none
        #   if newest reading end date is in this year
        #       increase the number of books read by one for correct page range

        i = 0
        while i < len(YearlyBooksPagesRead):
            if (YearlyBooksPagesRead[i][0] == None):
                print()
            elif YearlyBooksPagesRead[i][0].year == this_year:
                if YearlyBooksPagesRead[i][1] < 100:
                    self.book_pages_year["< 100"] += 1
                elif YearlyBooksPagesRead[i][1] < 200:
                    self.book_pages_year["100-200"] += 1
                elif YearlyBooksPagesRead[i][1] < 400:   
                    self.book_pages_year["200-400"] += 1 
                elif YearlyBooksPagesRead[i][1] < 600:   
                    self.book_pages_year["400-600"] += 1
                else:   
                    self.book_pages_year["> 600"] += 1  
            
            i += 1

        # return number of books read at each length 
        return self.book_pages_year

    def CalculateGenresPerYear(self): 
        # query to get newest reading end date and number of pages in the book for each book in the users collection - each book will have only oneneweest reading end date
        self.cursor.execute("SELECT C.NewestReadingEndDate, B.Genre FROM BookInUserCollection AS C, Book AS B WHERE C.email = %s AND B.APIid = C.ISBN;", [self.email])
        YearlyGenresRead = self.cursor.fetchall()

        this_year = datetime.date.today().year
        
        # dictionary of key value pairs - key: genre, value: number of books read in that genre
        self.num_genres_per_year = {}   
        # Add genres as keys as searching through database

        # if genre exists in dictionary already increase value by one
        # else add genre to dictionary
        i = 0
        while i < len(YearlyGenresRead):
            if (YearlyGenresRead[i][0] == None):
                print()
            elif(YearlyGenresRead[i][0].year == this_year):
                if(YearlyGenresRead[i][1] in self.num_genres_per_year):
                    self.num_genres_per_year[YearlyGenresRead[i][1]] += 1
                else:
                    self.num_genres_per_year[YearlyGenresRead[i][1]] = 1
            i += 1

        # return number of books for each genre read 
        return self.num_genres_per_year
    
    def CalcBookReread(self):
        self.cursor.execute("SELECT B.Title, C.NumberOfTimesReread FROM BookInUserCollection AS C, Book AS B WHERE C.email = %s AND B.APIid = C.ISBN AND C.NumberOfTimesReread > 1;", [self.email])
        BooksReread = self.cursor.fetchall()

        BookTitle = ""
        mostTimes = 0

        i = 0
        while(i < len(BooksReread)):
            if(mostTimes < BooksReread[i][1]):
                mostTimes = BooksReread[i][1]
                BookTitle = BooksReread[i][0]
            i += 1

        return BookTitle

    def CreateBarGraph(self, x, y, x_label, y_label, title):
        fig, ax = plt.subplots()

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))

        plt.bar(x, y, color = "#84A98C")
        # plt.title(title, fontproperties = self.font, fontsize = 20)
        plt.xlabel(x_label, fontproperties = self.font, fontsize = 15)
        plt.xticks(rotation = 45, fontproperties = self.font, fontsize = 10)
        plt.ylabel(y_label, fontproperties = self.font, fontsize = 15)
        plt.yticks(fontproperties = self.font, fontsize = 10)
        # fig.savefig('gersiteapp/static/gersiteapp/img/stats/BarGraph' + title.replace(' ', '') + '.png', bbox_inches='tight', transparent=True)
        

    def CreatePlotlyBarGraph(self, x_data, y_data, x_label, y_label):
        data = {x_label: x_data, y_label: y_data}
        df = DataFrame(data)
        fig = px.bar(df, x = x_label, y = y_label, color_discrete_sequence = ["#84A98C"])
        fig.update_layout(font_family = "Times New Roman", paper_bgcolor = "rgba(0,0,0,0)", plot_bgcolor = "rgba(0,0,0,0)", 
                          xaxis = {'tickformat': ',d'}, yaxis = {'tickformat': ',d'}, separators = "")
        fig.update_xaxes(type = 'category')
        bar_graph = py.offline.plot(fig, auto_open = False, output_type="div")
        return bar_graph


    def CreateLineGraph(self, x, y, x_label, y_label, title):
        fig, ax = plt.subplots()

        plt.plot(x, y, color = "#84A98C", linewidth = 5.0, marker = 'o', markersize = 10.0, markerfacecolor = "#004643")
        # plt.title(title, fontproperties = self.font, fontsize = 20)
        plt.xlabel(x_label, fontproperties = self.font, fontsize = 15)
        plt.xticks(rotation = 45, fontproperties = self.font, fontsize = 10)
        plt.ylabel(y_label, fontproperties = self.font, fontsize = 15)
        plt.yticks(fontproperties = self.font, fontsize = 10)

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))
        ax.set_xlim(x[0] - 1, x[-1] + 1)
        ax.set_ylim(0, max(y) + 3)

        # fig.savefig('gersiteapp/static/gersiteapp/img/stats/LineGraph' + title.replace(' ', '') + '.png', bbox_inches='tight', transparent=True)

    def CreatePlotlyLineGraph(self, x_data, y_data, x_label, y_label):
        data = {x_label: x_data, y_label: y_data}
        df = DataFrame(data)
        
        fig = px.line(df, x = x_label, y = y_label, color_discrete_sequence = ["#84A98C"], markers = True)
        fig.update_layout(font_family = "Times New Roman", paper_bgcolor = "rgba(0,0,0,0)", plot_bgcolor = "rgba(0,0,0,0)", 
                          xaxis = {'tickformat': ',d'}, yaxis = {'tickformat': ',d'}, separators = "")
        fig.update_xaxes(type = 'category')
        fig.update_traces(marker = dict (size = 11, color = "#004643", line = dict(width = 2, color = "#84A98C")))

        line_graph = py.offline.plot(fig, auto_open = False, output_type="div")
        return line_graph

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

        plt.pie(y, labels = x, startangle = 90, colors = PieColors, labeldistance = 1.1, explode = PieExplode, autopct='%1.1f%%', pctdistance = 1.25)
        # plt.legend()
        # plt.title(title, fontproperties = self.font, fontsize = 20)
        
        # fig.savefig('gersiteapp/static/gersiteapp/img/stats/PieChart' + title.replace(' ','') + '.png', bbox_inches='tight', transparent=True)


    def CreatePlotlyPieChart(self, x_label, y_data, title):
        PieColors = {}

        i = 0
        while i < len(x_label):
            if y_data[i] == 0:
                y_data.pop(i)
                x_label.pop(i)
            else:
                PieColors[x_label[i]] = ("#" + (str(hex(int(("#84A98C")[1:], 16) + 40*i)))[2:])
                i += 1

        data = {"Data" : y_data, "Label" : x_label}
        df = DataFrame(data)
        fig = px.pie(df, values = "Data", names = x_label, color = x_label, color_discrete_map = PieColors)
        fig.update_layout(font_family = "Times New Roman", paper_bgcolor = "rgba(0,0,0,0)", plot_bgcolor = "rgba(0,0,0,0)")
        
        pie_chart = py.offline.plot(fig, auto_open = False, output_type="div")
        return pie_chart

# if __name__ == '__main__':
#     books_per_month = {"January":5, "February": 7, "March": 10, "April": 10, "May": 0,
#         "June": 1, "July":4, "August": 8, "September": 1, "October": 0,
#         "November": 9, "December": 10}
#     x = list(books_per_month.keys())
#     y = list(books_per_month.values())
#     x_label = "Months"
#     y_label = "Number of Books read"
#     title = "Number of Books read each Month"
#     s = StatisticsModel("a@gmail.com")
#     s.CreateBarGraph(x, y, x_label, y_label, title)
#     s.CreatePieChart(x, y, title)
#     # s.NumPagesThisWeek()