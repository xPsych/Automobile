import mysql.connector
from mysql.connector import Error

try:
    mydb = mysql.connector.connect(host='localhost',
                                         database='Automobiles',
                                         user='Aswin',
                                         password='aswinkumar')
    if mydb.is_connected():
        db_Info = mydb.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = mydb.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
    
mycursor=mydb.cursor()

mycursor.execute('create table Customer_Details(CName varchar(25) primary key, CSno varchar(30), CDetails int, CAddress varchar(30), CPincode int, CIssue varchar(70), CParts varchar(30))')
