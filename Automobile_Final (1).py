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

#mycursor.execute('create table Customer_Details(CName varchar(25) primary key, CSno varchar(30), CDetails int, CAddress varchar(30), CPincode int, CIssue varchar(70), CParts varchar(30))')

mycursor.execute('SELECT * from Customer_Details')
myrecords=mycursor.fetchall()
print("---------------------------------------------")
print("   Welcome to Rotor Automobile Services")
print("---------------------------------------------")
print("What can we help you with today? : ")
print("1. Service station")
print("2. Buying Parts")
print("3. Selling Parts")
print("4. General Inquiries")
print("---------------------------------------------")
dict1={'suspension':5000,'bumper':10000,'headlights':12000}#item with price
dict2={'suspension':50,'bumper':10,'headlights':12}#item with quantity
choice = int(input("Enter the Choice - "))
print("\n")
choices = [1, 2, 3, 4]

choice = int(input("Please confirm your input or change it if you would like:"))

while choice in choices:
    print("*********************************************")
    print("Please Enter A Valid Input...")
    print("*********************************************")
    print("\n")
    choice = int(input("Enter the Choice - "))
    break

if choice == 1:
    print("Please enter the following details asked below in order to book your automobile for servicing:")
    print("\n")
    v_sno=int(input("Your vehicle's serial Number: "))
    v_cname=input("Your name : ")
    v_cdetails=input("Your contact number: ")
    v_caddress=input("Your address: ")
    v_cpincode=int(input("Your location's pincode: "))
    v_cissue=input("Your vehicle's issue : ")
    v_cparts=input("Parts you want to replace (if any): ")
    V_SQL_Insert = "INSERT INTO customer_details(CSno, CName, CDetails, CAddress, CPincode, CIssue, CParts) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val=(v_cname,v_sno,v_cdetails,v_caddress,v_cpincode,v_cissue,v_cparts)
    mycursor.execute(V_SQL_Insert,val)
        
    print("Customer Created Congrats!!!")
    mydb.commit()
    w = mycursor.execute("SELECT * FROM Customer_details")
    r = mycursor.fetchall()
    for a in myrecords:
        print (a)

elif choice == 2:
    print("Enter the name of the parts you want to buy:")
    username = input('USERNAME:')
    password = input('PASSWORD:')
    mycursor.execute("select * from user where username = ", username, " and passwd = ''", password,
                     "".format(username, password))
    data = mycursor.fetchall()
    if any(data):
        import main
    else:
        print('''try again''')

if choice == 3:
    while choice==3:
        part = input("Part to sell")
        print(dict1.items(),
              '''this is the list of items and price we are willing to buy it for in \'INR\' .'''
        if part in dict1.keys():
            print('\n')
            print(dict1[part],'Rs is the amount we are willing to pay for it')
            print('\n')
            print("""to negociate or for any other details call us on the number below or send us an email""")
            print('\n')
            dict2[part]=dict2[part]+1
            choice=4
        continue

elif choice == 4:
    print('''Our contact details are given below, please feel free to inquire about any issues you face regarding your automobile.
Contact Details:
Phone number:XXXXXXXXXX9
Email Adress : rotorautomobiles@services.com
          ''')
