import pymysql

# open data base connection
db = pymysql.connect(host='localhost',
                     user='root',
                     password='',
                     database='test')

# prepare a cursor object using cursor() method

cursor = db.cursor()

# execute sql quwery using execute method
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method
data = cursor.fetchone()
print("DataBase Version : %s " % data)

db.close()