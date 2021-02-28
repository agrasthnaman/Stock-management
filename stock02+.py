# STOCK MANAGEMENT
#SQL pw-12345
import os
import mysql.connector
import datetime
import string
import pyttsx3
now = datetime.datetime.now()

engine = pyttsx3.init()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    #wish the user.
    hour =int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning! welcome to stock management setup")
    elif hour >=12 and hour < 18:
        speak("Good Afternoon! welcome to stock management setup")
    else:
        speak("Good evening ! welcome to stock management setup")

def start():
    wishMe()
    #screen 1
    print("\t\t\t STOCK MANAGEMENT")
    print("\t\t\t ****************\n")
    print("\t\t 1. NEW STOCK")
    print("\t\t 2. OLD STOCK\n")
    speak("please select the fowlling options accordingly ")
    n=int(input("Enter your choice :"))
    
   
    if n== 1:
        print("\t 1. CREATE A NEW DATABASE")
        print("\t 2. OPEN MAIN MENU")
        print("\t 3. BACK\n")
        a=int(input("Enter your choice :"))
        if a==1:
           create_database()
           clrscr()
        if a==2:
            clrscr()
        if a==3:
            start()
    if n== 2:
         login2()

        

def login2():

    mydb=mysql.connector.connect(host="localhost",user="root",passwd="12345", database="stock")                              #as per system
    mycursor=mydb.cursor()
    a=input("Enter the user id.:")
    b=len(a)
    sql="SELECT uname FROM user where uname=%s"
    val=(a,)
    mycursor.execute(sql,val)
    c=mycursor.fetchall()
    f=str(c)
 
    if a==(f[3:b+3]):
        code=input("Enter the password:")
        z=len(code)
        abc="SELECT upwd FROM user where uname=%s"
        val=(a,)
        mycursor.execute(abc,val)
        x=mycursor.fetchall()
        w=str(x)
        if code==(w[3:z+3]):
            clrscr2()
    else:
        print("user name is invalid, plese try it again")
        login2()

def clrscr2():
    print("\n"*5)
    #screen 2.
    while True:
        print("\t\t\t STOCK MANAGEMENT")
        print("\t\t\t ****************\n")
        print("\t\t 1. PRODUCT MANAGEMENT")
        print("\t\t 2. PURCHASE MANAGEMENT")
        print("\t\t 3. SALES MANAGEMENT")
        print("\t\t 4. USER MANAGEMENT")
        print("\t\t 5. DATABASE SETUP")
        print("\t\t 6. EXIT")
        print("\t\t 7. CLOSE PC\n")
        speak("system welcomes you to the main screen")
        n=int(input("Enter your choice :"))
        if n== 1:
            product_mgmt()
        if n== 2:
            os.system('cls')
            purchase_mgmt()
        if n==3:
            sales_mgmt()
        if n== 4:
            user_mgmt( )
        if n==5:
            db_mgmt()
        if n== 6:
            speak("Thankyou for operating our program. Have nice day.")
            break
            
        if n==7:
            speak("pleas wait PC is soon going to be closed")
            sht()

def clrscr():
    #screen 2.
    print("\n"*5)
    while True:
        print("\t\t\t STOCK MANAGEMENT")
        print("\t\t\t ****************\n")
        print("\t\t 1. PRODUCT MANAGEMENT")
        print("\t\t 2. PURCHASE MANAGEMENT")
        print("\t\t 3. SALES MANAGEMENT")
        print("\t\t 4. USER MANAGEMENT")
        print("\t\t 5. DATABASE SETUP")
        print("\t\t 6. EXIT")
        print("\t\t 7. CLOSE PC\n")
        speak("system welcomes you to the main screen")
        n=int(input("Enter your choice :"))
        if n== 1:
            product_mgmt()
        if n== 2:
            os.system('cls')
            purchase_mgmt()
        if n==3:
            sales_mgmt()
        if n== 4:
            deft()
        if n==5:
            db_mgmt()
        if n== 6:
            speak("good bye")
            break
        if n==7:
            speak("pleas wait PC is soon going to be closed")
            sht()

def product_mgmt( ):
    while True :
        print("\t\t\t 1. Add New Product")
        print("\t\t\t 2. List Product")
        print("\t\t\t 3. Update Product")
        print("\t\t\t 4. Delete Product")
        print("\t\t\t 5. Back (Main Menu)")
        p=int (input("\t\tEnter Your Choice :"))
        if p==1:
            add_product()
        if p==2:
            search_product()
        if p==3:
            update_product()
        if p==4:
            delete_product()
        if p== 5:
            break

def purchase_mgmt( ):
    while True :
        print("\t\t\t 1. Add Order")
        print("\t\t\t 2. List Order")
        print("\t\t\t 3. Back (Main Menu)")
        o=int(input("\t\tEnter Your Choice :"))
        if o==1 :
            add_order()
        if o==2 :
            list_order()
        if o== 3 :
            break

def sales_mgmt( ):
    while True :
        print("\t\t\t 1. Sale Items")
        print("\t\t\t 2. List Sales")
        print("\t\t\t 3. Back (Main Menu)")
        s=int (input("\t\tEnter Your Choice :"))
        if s== 1 :
            sale_product()
        if s== 2 :
            list_sale()
        if s== 3 :
            break

def user_mgmt( ):
    speak("welcome to user management option")
    while True :
        print("\t\t\t 1. Add user")
        print("\t\t\t 2. List user")
        print("\t\t\t 3. Back (Main Menu)")
        u=int (input("\t\tEnter Your Choice :"))
        if u==1:
            add_user()
        if u==2:
            list_user()
        if u==3:
            break
def deft():
    speak("please enter the management password")
    a=input("Enter the management password:")
    if a=='stock@management':
        user_mgmt()
    else:
        print("Password is incorrect, please try again")
        deft()
     
def create_database():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="12345",database="stock")				#change as per system
    mycursor=mydb.cursor()
    speak("please wait , till the pc makes the required setup.")
    print(" Creating PRODUCT table")
    sql = "CREATE TABLE if not exists product (\
            pcode int(4) PRIMARY KEY,\
            pname char(30) NOT NULL,\
            pprice float(8,2) ,\
            pqty int(4) ,\
            pcat char(30));"
    mycursor.execute(sql)
    print("PRODUCT table created")
    print(" Creating ORDER table")
    sql = "CREATE TABLE if not exists orders (\
            orderid int(4)PRIMARY KEY ,\
            orderdate DATE ,\
            pcode char(30) NOT NULL , \
            pprice float(8,2) ,\
            pqty int(4) ,\
            supplier char(50),\
            pcat char(30));"
    mycursor.execute(sql)
    print(" ORDER table created")

    print(" Creating SALES table")
    sql = "CREATE TABLE if not exists sales (\
            salesid int(4) PRIMARY KEY ,\
            salesdate DATE ,\
            pcode char(30) references product(pcode), \
            pprice float(8,2) ,\
            pqty int(4) ,\
            Total double(8,2)\
            );"
    mycursor.execute(sql)
    print(" SALES table created")
    print(" Creating USER table")
    sql = "CREATE TABLE if not exists user (\
            uid char(35) PRIMARY KEY,\
            uname char(30) NOT NULL,\
            upwd varchar(30));"
    mycursor.execute(sql)
    print(" USER table created")
    speak("program is sucessfully setup in your system !")

def list_database():
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="12345",database="stock")   				#as per system
        mycursor=mydb.cursor()
        sql="show tables;"
        mycursor.execute(sql)
        for i in mycursor:
            print(i)

def add_order():
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="12345",database="stock")				#as per system
            mycursor=mydb.cursor()
            now = datetime.datetime.now()
            sql="INSERT INTO orders (orderid, orderdate, pcode, pprice, pqty, supplier, pcat) values (%s,%s,%s,%s,%s,%s,%s)"
            code=int(input("Enter product code :"))
            oid=now.year+now.month+now.day+now.hour+now.minute+now.second
            qty=int(input("Enter product quantity : "))
            price=float(input("Enter Product unit price: "))
            cat=input("Enter product category: ")
            supplier=input("Enter Supplier details: ")           
            val=(oid,now,code,price,qty,supplier,cat)
            mycursor.execute(sql,val)
            mydb.commit()



def list_order():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="12345", database="stock")					#as per system
    mycursor=mydb.cursor()
    sql="SELECT * from orders"
    mycursor.execute(sql)
    print("\t\t\t\t\t\t\t ORDER DETAILS")
    print("-"*120)
    print("orderid          Date                Product code             price              quantity           Supplier        Category")
    print("-"*120)
    for i in mycursor:
         print(i[0],"\t",i[1],"\t",i[2],"\t   ",i[3],"\t",i[4],"\t     ",i[5],"\t",i[6])
         print("-"*120)
                    

def db_mgmt( ):
    while True :
        print("\t\t\t 1. Database creation")
        print("\t\t\t 2. List Database")
        print("\t\t\t 3. Back (Main Menu)")
        p=int (input("\t\tEnter Your Choice :"))
        if p==1 :
            create_database()
        if p==2 :
            list_database()
        if p== 3 :
            break
def add_product():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="12345",database="stock")				    #as per system
    mycursor=mydb.cursor()
    sql="INSERT INTO product(pcode,pname,pprice,pqty,pcat) values (%s,%s,%s,%s,%s)"
    code=int(input("\t\tEnter product code :"))
    search="SELECT count(*) FROM product WHERE pcode=%s;"
    val=(code,)
    mycursor.execute(search,val)
    for x in mycursor:
        cnt=x[0]
        cnt==0
        name=input("\t\tEnter product name :")
        qty=int(input("\t\tEnter product quantity :"))
        price=float(input("\t\tEnter product unit price :"))
        cat=input("\t\tEnter Product category :")
        val=(code,name,price,qty,cat)
        mycursor.execute(sql,val)
        mydb.commit()
    else:
        print("\t\t Product already exist")
def update_product():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="12345",database="stock")                                   #as per system
    mycursor=mydb.cursor()
    code=int(input("Enter the product code :"))
    qty=int(input("Enter the quantity :"))
    sql="UPDATE product SET pqty=pqty+%s WHERE pcode=%s;"
    val=(qty,code)
    mycursor.execute(sql,val)
    mydb.commit()
    print("\t\t Product details updated")

def delete_product():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="12345",database="stock")                               #as per system
    mycursor=mydb.cursor()
    code=int(input("Enter the product code :"))
    sql="DELETE FROM product WHERE pcode = %s;"
    val=(code,)
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount," record(s) deleted");

def search_product():

    while True :
        print("\t\t\t 1. List all product")
        print("\t\t\t 2. List product code wise")
        print("\t\t\t 3. List product categoty wise")
        print("\t\t\t 4. Back (Main Menu)")
        s=int(input("\t\tEnter Your Choice :"))
        if s==1 :
            list_product()
        if s==2 :
            code=int(input(" Enter product code :"))
            list_prcode(code)
                                      
        if s==3 :
            cat=input("Enter category :")
            list_prcat(cat)
                                     
        if s==4 :
            break

def list_product():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="12345",database="stock")                       #as per system
    mycursor=mydb.cursor()
    sql="SELECT * from product"
    mycursor.execute(sql)
    print("\t\t\t\t PRODUCT DETAILS")
    print("\t\t","-"*95)
    print("\t\t code          name                            price               quantity                     category")
    print("\t\t","-"*95)
    for i in mycursor:
        print("\t\t",i[0],"\t",i[1],"\t\t     ",i[2],"\t  ",i[3],"\t\t    ",i[4])
        print("\t\t","-"*95)


def list_prcode(code):
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="12345",database="stock")
    mycursor=mydb.cursor()
    sql="SELECT * from product WHERE pcode=%s"
    val=(code,)
    mycursor.execute(sql,val)
    print("\t\t\t\t PRODUCT DETAILS")
    print("\t\t","-"*47)
    print("\t\t code    name    price   quantity      category")
    print("\t\t","-"*47)
    for i in mycursor:
        print("\t\t",i[0],"\t",i[1],"\t",i[2],"\t   ",i[3],"\t\t",i[4])
        print("\t\t","-"*47)


def sale_product():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="12345",database="stock")                               #as per system
    mycursor=mydb.cursor()
    pcode=input("Enter product code: ")
    sql="SELECT count(*) from product WHERE pcode=%s;"
    val=(pcode,)
    mycursor.execute(sql,val)
    for x in mycursor:
        cnt=x[0]
    if cnt !=0 :
        sql="SELECT * from product WHERE pcode=%s;"
        val=(pcode,)
        mycursor.execute(sql,val)
        for x in mycursor:
            print(x)
            price=int(x[2])
            pqty=int(x[3])
            qty=int(input("Enter no of quantity :"))
        if qty <= pqty:
            total=qty*price;
            print ("Collect  Rs. ", total)
            sql="INSERT into sales values(%s,%s,%s,%s,%s,%s)"
            val=(int(cnt)+1,datetime.datetime.now(),pcode,price,qty,total)
            mycursor.execute(sql,val)
            sql="UPDATE product SET pqty=pqty-%s WHERE pcode=%s"
            val=(qty,pcode)
            mycursor.execute(sql,val)
            mydb.commit()
        else:
            print(" Quantity not Available")
    else:
        print(" Product is not avalaible")

def list_sale():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="12345",database="stock")                               #as per system
    mycursor=mydb.cursor()
    sql="SELECT * FROM sales"
    mycursor.execute(sql)
    print(" \t\t\t\tSALES DETAILS")
    print("-"*80)
    print("Sales id  Date          Product Code           Price                 Quantity                 Total")
    print("-"*80)
    for x in mycursor: 
        print(x[0],"\t",x[1],"\t",x[2],"\t   ",x[3],"\t\t",x[4],"\t\t",x[5])
        print("-"*80)
                                     
                                  
def list_prcat(cat):
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="12345",database="stock")                   #as per system
    mycursor=mydb.cursor()
    print (cat)
    sql="SELECT * from product WHERE pcat =%s"
    val=(cat,)
    mycursor.execute(sql,val)
    clrscr()
    print("\t\t\t\t PRODUCT DETAILS")
    print("\t\t","-"*97)
    print("\t\t code           name               price         quantity                category")
    print("\t\t","-"*97)
    for i in mycursor:
        print("\t\t",i[0],"\t",i[1],"\t",i[2],"\t   ",i[3],"\t\t",i[4])
        print("\t\t","-"*97)

def add_user():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="12345",database="stock")                           #as per system
    mycursor=mydb.cursor()
    uid=input("Enter emaid id :")
    name=input(" Enter Name :")
    paswd=input("Enter Password :")
    sql="INSERT INTO user values (%s,%s,%s);"
    val=(uid,name,paswd)
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount, " user created")


def list_user():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="12345",database="stock")                       #as per system
    mycursor=mydb.cursor()
    sql="SELECT uid,uname from user"
    mycursor.execute(sql)
    print("\t\t\t\t USER DETAILS")
    print("\t\t","-"*67)
    print("\t\t UID                                           name    ")
    print("\t\t","-"*67)
    for i in mycursor:
        print("\t\t",i[0],"\t",i[1])
        print("\t\t","-"*67)


def sht():
    os.system("shutdown /s /t 1")
        
start()
