filePath = './Inputs/Distances.csv'
with open(filePath,'r') as file:
#file = open(filePath, 'r')
    for line in file.readlines():
        print(line)
        print(line.split(','))
    file.close()


#conection to SQLite which is, by default, installed with Pyhton3
import sqlite3
con = sqlite3.connect(":memory:") #create DB in memory
cur = con.cursor()

sql_script_file = "/media/p0400533/7581-F871/Projet Lif/Inputs/villes_france.sql"
with open(sql_script_file,'r') as sqlScript:
    cur.executescript(sqlScript.read())
    sqlScript.close
