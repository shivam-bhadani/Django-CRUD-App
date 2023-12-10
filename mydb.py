import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'Your DB Username here',
    passwd = 'Your DB Password here'
)

# prepare a cursor object

cursorObject = database.cursor()

#create a database
cursorObject.execute("CREATE DATABASE dcrmDB")

print("All Done!")