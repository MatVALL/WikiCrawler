import mysql.connector
import sys

def connect(database="wiki_crawl"):
    return mysql.connector.connect(
      host="localhost",
      user="mv",
      password="plz_dont_hack",
      database=database
    )

class websiteDBConnector():
    def __init__(self,database='wiki_crawl',table='websites'):
        self.database_name = database
        self.database = connect(database)#necessaire de le garder, sinon est garbage collecté et cursor ne pointe plus sur rien
        self.cursor = self.database.cursor()
        self.table = table
    #juste pour rappel
    def createDB(self,name):
        self.cursor.execute("CREATE DATABASE "+name)
    #table of website
    def createTableWebsites(self):
        request = "CREATE TABLE "+ self.database+" (\
            adress VARCHAR(255) PRIMARY KEY,\
            name VARCHAR(255) NOT NULL,\
            description TEXT\
        )"
        self.cursor.execute(request)
#mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
    def dropWebsite(self):
        self.cursor.execute("DROP TABLE "+table)
    def isInDB(self, adress):
        request = "SELECT adress FROM "+self.table+" WHERE adress=\'"+adress+"\'"
        self.cursor.execute(request)
        return self.cursor.fetchall()!=[]
    def addWebsiteDB(self,adress, name, description):
        if(self.isInDB(adress)):
            print("Attempting to add an existing website :" +adress)
            print("Skipped.")
            return
        sql = "INSERT INTO "+self.table+" (adress, name, description) VALUES (%s, %s, %s)"
        val = (adress, name, description)
        self.cursor.execute(sql, val)
        self.database.commit()
    def printDB(self):
        print("!!")
        request = "SELECT * FROM "+self.table
        self.cursor.execute(request)
        for line in self.cursor.fetchall():
            print(line)
    def empty_table(self):
        raise(NotImplementedError)
if __name__=='__main__':
    con=websiteDBConnector()
    con.addWebsiteDB('a', 'b', 'c')
    con.addWebsiteDB('d', 'e', 'f')
    con.addWebsiteDB('g', 'h', 'i')
    con.printDB()
    con.empty_table()
