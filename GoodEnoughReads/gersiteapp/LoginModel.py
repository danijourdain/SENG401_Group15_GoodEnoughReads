import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from django.db import models
from django.db import connection, transaction
import datetime

class CollectionModel:
    def __init__(self, email):
        self.email = email
        self.cursor = connection.cursor()

    def retrieveAccountInfo(self, email):
        self.cursor.execute("SELECT * FROM User WHERE email = '"+email+"';")
        accInfo = self.cursor.fetchall()
        return accInfo
