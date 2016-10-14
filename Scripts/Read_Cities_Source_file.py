#!/usr/bin/python3.2

#set current working directory
from sys import path
from os import chdir
#chdir("C:/Users/Joe/Documents/GitHub/LifeProject/Scripts")
#chdir("/home/etu/f/p0400533/LifeProject-master/Scripts")
chdir(path[0])

#import distances between main european towns
filePath = '../Inputs/Distances.csv'

townMatrix = dict() #stores all the cities with the distance between the other cities
townList = list()
#open Distance file
with open(filePath,'r') as file:

    isHeader = True #first row is an header row which is not relevant for the moment
    for line in file.readlines():
        if isHeader:
            isHeader = False #skip the first row
        else:
            row = line.split(',') #data are imported from a csv with ',' as a separator
            town = row[0]
            townList.append(town)
            # for i in range(len(townList)) :
            #     townMatrix[town].update((townList[i],row[i]))

            #print(line)
            #beware, there are 3 extra columns for Stockholm, Vienna and Warsaw
            #print(line.split(','))
    file.close()

print(townMatrix)
print(townList)
print(townMatrix.keys())

#conection to SQLite which is, by default, installed with Pyhton3
# import sqlite3
# con = sqlite3.connect(":memory:") #create DB in memory
# cur = con.cursor()
# 
# sql_script_file = "/media/p0400533/7581-F871/Projet Lif/Inputs/villes_france.sql"
# with open(sql_script_file,'r') as sqlScript:
#     cur.executescript(sqlScript.read())
#     sqlScript.close
#import sys
#print(sys.path[0])