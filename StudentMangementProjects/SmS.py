from tabulate import tabulate
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mid666??",
    database="stms"
)

def select():
    cur=mydb.cursor()
    sql="select id,NAME,AGE,DEPT,PLACE from student"
    cur.execute(sql)
    result=cur.fetchall()
    print(tabulate(result,headers=["id","NAME","AGE","DEPT","PLACE"]))

def insert(NAME,AGE,DEPT,PLACE):
    cur=mydb.cursor()
    sql="insert into student (NAME,AGE,DEPT,PLACE) values(%s,%s,%s,%s)"
    user=(NAME,AGE,DEPT,PLACE)
    cur.execute(sql,user)
    mydb.commit()
    print("DATA Inserted Succesfully")
    
def update(NAME,AGE,DEPT,PLACE,id):
    cur=mydb.cursor()
    sql="update student set NAME=%s,AGE=%s,DEPT=%s,PLACE=%s where id=%s"
    user=(NAME,AGE,DEPT,PLACE,id)
    cur.execute(sql,user)
    mydb.commit()
    print("DATA UPDATED Succesfully")

def delete(id):
    cur=mydb.cursor()
    sql="delete from student where id=%s"
    user=[id]
    cur.execute(sql,user)
    mydb.commit()
    print("DATA Deleted Succesfully")
def EXIT():
    print("ok")


while True:
    print("1.SELECT")
    print("2.INSERT")
    print("3.UPDATE")
    print("4.DELETE")
    print("5.EXIT")
    choice=int(input("Enter The choice: "))

    if choice==1:
        select()
    elif choice==2:
        NAME=input("Enter The  Name: ")
        AGE=int(input("Enter The  Age: "))
        DEPT=input("Enter The  Department: ")
        PLACE=input("Enter The  Place: ")
        insert(NAME,AGE,DEPT,PLACE)
    elif choice==3:
        id=int(input("Enter The Id: "))
        NAME=input("Enter The  Name: ")
        AGE=int(input("Enter The  Age: "))
        DEPT=input("Enter The  Department: ")
        PLACE=input("Enter The  Place: ")
        update(NAME,AGE,DEPT,PLACE,id)
    elif choice==4:
        id=int(input("Enter The Id: "))
        delete(id)
    elif choice==5:
        EXIT()
    else:
        print("Invalid Choice")
        print('Please Check Your Choice You Selected')



