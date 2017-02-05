# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 09:11:31 2016

@author: Marco_Zeng
"""

#!/usr/bin/python

import sqlite3
test1 = sqlite3.connect('D:\Develop\SQLiteDB\Test1.db')
print("Opened database successfully")

cursor = test1.execute("Select Id, Name, Age, Score from Student")
for row in cursor:
    print("ID = ", row[0])
    print("Name = ", row[1])
    print("Age = ", row[2])
    print("Score = ", row[3], "\n")

print("Operation done successfully")
test1.close()
print(value)
