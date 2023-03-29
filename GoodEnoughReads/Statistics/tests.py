# from django.test import TestCase
# from mock import patch
# import unittest
# from . import StatisticsModel
# from django.db import connection
# import MySQLdb
# import pymysql
# from ManageAccount import LoginModel 

# class StatisticsTestCase(unittest.TestCase):
    # databases = '__all__'
    
    # def setUp(self):
    #     self.conn = pymysql.connect(host='localhost', user='ger', password='seng', db='ger_db')
    #     self.cursor = self.conn.cursor()
    #     self.cursor.execute("INSERT INTO User(email, `Name`, XP, AwardProfile) VALUES (\"sobia@gmail.com\", \"a\", 0, 0);")
    #     self.stats = StatisticsModel.StatisticsModel("sobia@gmail.com")
    #     # result = cursor.fetchall()
    #     # print(result)

    # def tearDown(self) -> None:
    #     self.conn.close()
    #     return super().tearDown()

    # def test_num_pages_correct(self):
    #     numPages = self.stats.NumPagesThisWeek()
    #     self.assertEqual(numPages, 0)

    # def test_awards_page_url(self):
    #     response = self.client.get("/awards/")
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, template_name='Awards/awards.html')

    # def test_statistics_page_url(self):
    #     response = self.client.get("/statistics/")
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, template_name='Statistics/statistics.html')