import mysql.connector
import sys

#juste pour rappel
def createDB(cursor,name):
    cursor.execute("CREATE DATABASE "+name)

#table of website
def createTableWebsites(cursor):
    request = "CREATE TABLE websites (\
        adress VARCHAR(255) PRIMARY KEY,\
        name VARCHAR(255) NOT NULL,\
        description TEXT\
    )"
    cursor.execute(request)
#mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
def dropWebsite():
    cursor.execute("DROP TABLE websites")

def connect(database="wiki_crawl"):
    return mysql.connector.connect(
      host="localhost",
      user="mv",
      password="plz_dont_hack",
      database=database
    )

def isInDB(cursor, adress):
    sql = "SELECT adress FROM websites WHERE adress=\'"+adress+"\'"
    print(sql)
    cursor.execute(sql)
    return cursor.fetchall()!=[]

def addWebsiteDB(cursor,adress, name, description):
    if(not isInDB(cursor,adress)):
        sql = "INSERT INTO websites (adress, name, description) VALUES (%s, %s, %s)"
        val = (adress, name, description)
        cursor.execute(sql, val)
        mydb.commit()

if __name__=='__main__':
    mydb= connect()
    cursor = mydb.cursor()
#    createTableWebsites(cursor)
    addWebsiteDB(cursor,"http://www.wikipedia.org", 'Main page', "La page d'acceuil wiki")
    cursor.execute("SHOW TABLES")
    for x in cursor:
        print(x)
    print(cursor.rowcount, "row count.")
