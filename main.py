#Online crime reporting system for minors(age<=18)(T1) and registration of social complaints(T2)
#Default password of both tables is Admin
#table 1 name, dob,institute, crime, mobileno,address ,rdate , complaintcode, status
#table 2 complaint , complaint_area, your_name, mobile_no,r_date,  status, your_complaint_no


import MySQLdb
import os
import random 
import time
from prettytable import PrettyTable
from datetime import date
from datetime import datetime

def current():
    now=datetime.now()
    print("Today's date and time are: ",now.strftime("%d/%m/%y  %H:%M:%S"))
    print("")
current()

#MySQL passwrd
sql_passwrd=input("Enter your MYSQL passwrd:")
print("")
    
#Connection

def connection():
    global c
    global mydb
    mydb=MySQLdb.connect(host="localhost",\
    user="root",\
    passwd=sql_passwrd)
    c=mydb.cursor()
connection()

#Database

def DATABASE():
    
    try:
        c.execute("create database sarthakdldav")
        c.execute("use sarthakdldav")
    except:
        c.execute("use sarthakdldav")
        pass
    c.execute("use sarthakdldav")
    try:
        c.execute("use sarthakdldav")
        c.execute("create table crime(name varchar(50) not null, DOB date not null,institute varchar(100), crime varchar(20) not null, mobileno varchar(10) not null, address varchar(100),rdate date, complaintcode varchar(50), status varchar(50))")
        c.execute("create table clean(complaint varchar(100) not null, complaint_area varchar(100) not null, your_name varchar(50) not null, mobile_no varchar(11) not null, r_date date, your_status varchar(50),your_complaint_no varchar(50))")
        c.execute("create table a_passwrd(admin_passwrd varchar(100) not null)")
        c.execute("create table aa_passwrd(aadmin_passwrd varchar(100) not null)")
        mydb.commit()
    except:
        c.execute("use sarthakdldav")
        pass
    
    try:
        sql_="insert into a_passwrd values (%s)"
        c.execute(sql_,("Admin",))
        mydb.commit()
    except:
        pass
    try:
        c.execute("use sarthakdldav")
        sql="insert into aa_passwrd values (%s)"
        c.execute(sql,("Admin",))
        mydb.commit()
    except:
        c.execute("use sarthakdldav")
        pass
DATABASE()

#Pretty Table
def pretty_table():
    global s
    global ptable
    global ptable2
    s = PrettyTable()
    s.field_names = ["Name", "DOB", "Inst.", "Crime", "Mob.no.", "Add." , "RDate", "Comp.Code", "Status"]
    ptable = PrettyTable()
    ptable.field_names = ["Complaint", "Comp._area", "Name", "Mob.no.", "RDate", "Status", "Comp.no."]
    ptable2=PrettyTable()
    ptable2.field_names=["Your Password"]
pretty_table()

today = date.today()

#Start menu
while True:
    print("Press 1 for social complaints")
    print("OR")
    print("Press 2 for crime complaints")
    print("")
    OPTION=input("Enter the option to continue:")
    print("")

    if OPTION=="2" or OPTION=="2":

#Start of table1
#Crime complaints

        print("Welcome to AKSJ online crime reporting sysytem ")
        print("")
        print("Select from one of the following options")
        print("A. Admin")
        print("B. User")
        print("S. Check Complaint status")
        OPTION3=input("Enter A/B/S to continue:")
        print("")

        if OPTION3=="A" or OPTION3=="a":
            print("U have choosen Admin!!")
            print("")
            admin_passwrd2=input("Enter your password:")
            sql="Select * from a_passwrd"
            c.execute(sql,)

            for i in c:
                INDEX_NO=i
                #print(INDEX_NO)
                #print(INDEX_NO[0])
            INDEX2=INDEX_NO[0]

            state4=True

            while state4==True:

                if admin_passwrd2==INDEX2:
                    print("")
                    print("")
                    print("A1- show all complaints")
                    print("A2- to update existing complaints")
                    print("A3- to show complaints of a particular month")
                    print("A4- to change your password")
                    print("DD- clear all records ")
                    print("A5- to exit")
                    print("")
                    menu_options2=input("Choose an option from above:")

                    if menu_options2=="A1" or menu_options2=="a1":
                        s.clear_rows()
                        sqlite_select_query = """SELECT * from crime"""
                        c.execute(sqlite_select_query)
                        records = c.fetchall()
                        for row in records:
                            s.add_row(row)
                        print(s)

                    elif menu_options2=="A5" or menu_options2=="a5":
                        break

                    elif menu_options2=="dd" or menu_options2=="DD":
                        sql="delete from crime"
                        c.execute(sql,)
                        mydb.commit()
                        print("Command successfully executed!")

                    #Show records b/w particular dates

                    elif menu_options2=="A3" or menu_options2=="a3":
                        d1=input("Enter initial date:(in yy-mm-dd): ")
                        d2=input("Enter final date (in yy-mm-dd): ")
                        print("Records r being shown b/w",d1,"and",d2)
                        print("")
                        sqlite_select_query = """SELECT count(*) from crime where rdate>%s and rdate<%s"""
                        c.execute(sqlite_select_query,(d1,d2))
                        records = c.fetchall()
                        s.clear_rows
                        print("No. of records are:",records[0][0])
                        print("")
                        sqlite_select_query = """SELECT * from crime where rdate>%s and rdate<%s"""
                        c.execute(sqlite_select_query,(d1,d2))
                        records=c.fetchall()

                        for row in records:
                            s.add_row(row)
                            print(s)

                    #Change password
                    elif menu_options2=="A4" or menu_options2=="a4":
                        def update_passwrd():
                            passwrd1=(input("Enter old password:"))

                            if passwrd1==admin_passwrd2:
                                passwrd2=(input("Enter the new password:"))
                                rpasswrd1=(input("Enter the new password again:"))

                                if passwrd2==rpasswrd1:
                                    sql="update a_passwrd set admin_passwrd=%s"
                                    c.execute(sql,(passwrd2,))

                                    for LIST in [4,3,2,1]:
                                        print("Waiting for %s" % LIST, end='')
                                        print(" Sec")
                                        time.sleep(LIST)
                                    print("Successfully changed!")
                                    mydb.commit()
                                    
                                else:
                                    return print("Your entered passwrd didn't match!")
                                    pass
                                    
                            else:
                                return print("Your entered password didn't match!")
                                pass
                                
                        update_passwrd()

                    #Update complaint ststus
                    elif menu_options2=="A2" or menu_options2=="a2":
                        print("")
                        complaintcode=input("Enter complaint code which u want to update:")
                        status=input("Type what do u want to add as status:")
                        sql="update crime set status=%s where complaintcode=%s"
                        c.execute(sql,(status,complaintcode,))
                        print("")
                        print("Succesfully changed!")
                        print("")
                        mydb.commit()
                else:
                    print("wrong password!!")
                    print("Try again !")
                    print("")
                    break

        #User interface
        elif OPTION3=="B" or OPTION3=="b":
            print("U r a common user!!")
            age=int(input("enter your age:"))

            if age<=18:
                print("U r a minor!")
                print("")
                DOB33=input("Enter your DOB year:")
                dob_digit1=DOB33[2]
                dob_digit2=DOB33[3]
                n3=dob_digit1+dob_digit2
                n4=int(n3)
                today=date.today()
                d2 = today.strftime("%y")
                user_date=int(d2)
                dob1=user_date-n4
                dob2=user_date-n4-1
                dob3=user_date-n4+1

                if dob1==age or dob2==age or dob3==age :
                    print("Age verified!")
                    print("")

                    n=eval(input("Enter the no. of complaints u want  to register:"))

                    for j in range(0,n):
                        print("For DOB:")
                        DOB1=input("Enter your DOB day:")
                        DOB2=input("Enter your DOB month:")
                        name=(input("enter your name:"))
                        DOB=DOB33+"-"+DOB2+"-"+DOB1
                        institute=input("Enter the name of institution studying in:")
                        m1="harrassment"
                        m2="Domestic_voilence"
                        m3="Child_labour"
                        m4="Minor_rape_case"
                        m5="Cyber_bullying"
                        m6="Mising_person_or_valuable_objects"
                        m7="Fraud_case"
                        m8="Bad_touch"
                        m9="Drug_case"
                        print("")
                        print("SOME COMMON CRIME TYPES:")
                        print("m1-Harrassment")
                        print("m2-Domestic  violence")
                        print("m3-Child labour")
                        print("m4-Minor Rape case ")
                        print("m5-Cyber bullying")
                        print("m6-Missing person/ valuable objects")
                        print("m7-Fraud case")
                        print("m8-Bad touch")
                        print("m9-Drug case")
                        print("If your crime type is other than these, Then ")
                        print("")
                        print("Type yourself:")
                        print("")
                        crime1=input("Enter crime type no. from above options:")
                        crime= m1 or m2 or m3 or m4 or m5 or m6 or m7 or m8 or m9 or crime1
                        mobileno=input("Enter your 10 digit mobile no. :")
                        length_no=len(mobileno)
                        if length_no==10:
                            pass
                        else:
                            print("Mobile no doesn't match requirments!")
                            print("")
                            break
                        address=input("Enter your complete address:")
                        d1 = today.strftime("%y-%m-%d")
                        rdate = d1
                        #yu=random.randint(0,1000)
                        #yuu=str(yu)
                        complaintcode= mobileno+"@"+str(DOB33+DOB2+DOB1)
                        status="Pending"
                        print("")

                        state=True

                        while state==True:
                            random_no=random.randint(0,10000)
                            print("Verify that u r not A ROBOT!")
                            print(random_no)
                            CAPTCHA=eval(input("Enter the captcha seen:"))

                            if CAPTCHA==random_no:
                                print("")
                                print("Pass!")
                                print("")
                                state=False

                            else:
                                print("Retry")
                                print("")
                            
                        print("Thank u. Your complaint has been registered:)")
                        print("Your complaint code is:", complaintcode)
                        print("")
                        print("")
                        sql="insert into crime (name, DOB, institute, crime, mobileno, address , rdate , complaintcode, status) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                        c.execute(sql,(name, DOB, institute, crime, mobileno, address ,rdate ,complaintcode, status,))
                        mydb.commit()

                elif dob1!=age or dob2!=age or dob3!=age:
                    print("Your age and DOB year doesn't match!")
                    break

            elif age>18:
                print("U r an adult!")
                break

        elif OPTION3=="s" or OPTION3=="S":
            print("")
            COMPLAINT_NO=input("Enter your compliant code:")
            c.execute("select status from crime where complaintcode=%s",(COMPLAINT_NO,))
            records = c.fetchall()
            print("status: ",records[0][0])

#End of table 2

#Start of table 2
            
    elif OPTION=="1" or OPTION=="1":
        print("")
        print("Welcome to AKSJ online social complaints reporting system")
        print("")
        print("Select from one of the following options")
        print("A1. Admin login")
        print("B1. User")
        print("S1. Complaint status")
        OPTION2=input("Enter A1/B1/S1 to continue:")
        print("")

        if OPTION2=="A1" or OPTION2=="a1":
            print("U have choosen Admin!!")
            print("")
            admin_passwrd=input("Enter your password:")
            sql="select * from aa_passwrd"
            c.execute(sql,)

            #Finding passwrd from table
            for i in c:
                INDEX=i[0]

            state1=True

            while state1==True:

                if admin_passwrd==INDEX:
                    print("WELCOME!")
                    print("")
                    print("A6- show all complaints ")
                    print("A7- to update existing complaints ")
                    print("A8- to chage passwrd")
                    print("A9- to view complaints of a particular month")
                    print("A10- clear all records")
                    print("A11-to exit")
                    print("")
                    menu_option=input("Choose an option from above:")

                    if menu_option=="A6" or menu_option=="a6":
                        ptable.clear_rows()
                        sqlite_select_query = """SELECT * from clean"""
                        c.execute(sqlite_select_query)
                        records = c.fetchall()
                        for row in records:
                            ptable.add_row(row)
                        print(ptable)

                    elif menu_option=="A10" or menu_option=="a10":
                        sql="delete from clean"
                        c.execute(sql,)
                        mydb.coomit()
                        print("Command successfully executed!")

                    #Display records b/w particular dates
                    elif menu_option=="A9" or menu_option=="a9":
                        date_input=input("Enter initial date:(in yy-mm-dd): ")
                        user_date=input("Enter final date (in yy-mm-dd): ")
                        print("Records r being shown b/w",date_input,"and",user_date)
                        print("")
                        sqlite_select_query = """SELECT count(*) from clean where r_date>%s and r_date<%s"""
                        c.execute(sqlite_select_query,(date_input,user_date)) 
                        records = c.fetchall()
                        s.clear_rows
                        print("No. of records are:",records[0][0])
                        print("")

                        for row in records:
                            s.add_row(row)
                            print(s)

                    #Change passwrd
                    elif menu_option=="A8" or menu_option=="a8":
                        def update_passwrd():
                            old_passwrd=(input("Enter old password:"))
                            if old_passwrd==admin_passwrd:
                                passwrd3=(input("Enter the new password:"))
                                rpasswrd2=(input("Enter the new password again:"))
                                if passwrd3==rpasswrd2:
                                    sql="update aa_passwrd set aadmin_passwrd=%s"
                                    c.execute(sql,(passwrd3,))
                                    for LIST in [4,3,2,1]:
                                        print("Waiting for %s" % LIST, end='')
                                        print(" Sec")
                                        time.sleep(LIST)
                                    print("Successfully changed!")
                                    mydb.commit()
                                    
                                else:
                                    print("Your entered passwrd didn't match!")
                                    pass

                            else:
                                print("Your entered password didn't match!")
                                pass
                                
                                
                        update_passwrd()

    
                     #Update complaint status
                    elif menu_option=="A7" or menu_option=="a7":
                        print("")
                        your_complaint_no=input("Enter complaint no which u want to update:")
                        your_status=input("Type what do u want to add as status:")
                        sql="update clean set your_status=%s where your_complaint_no=%s"
                        c.execute(sql,(your_status,your_complaint_no,))
                        print("Successfully Updated!")
                        mydb.commit()
                            
                    elif menu_option=="A11" or menu_option=="a11":
                        break
                else:
                    print("Wrong password! ")
                    break
                

        #User interface
        elif OPTION2=="B1" or OPTION2=="b1":
            RECORD_NO=eval(input("How many complaints do u want to register:"))
            for i in range(0,RECORD_NO):
                complaint=input("Enter the complaint:")
                complaint_area=input("Enter the complaint location:")
                your_name=input("Enter your full name")
                mobile_no=input("Enter the 10 digit mobile no.: ")
                d1 = today.strftime("%Y-%m-%d")
                r_date = d1
                RANDOM_NO2=random.randint(0,1000)
                RANDOM_NO21=str(RANDOM_NO2)
                your_complaint_no=mobile_no+"@"+RANDOM_NO2
                your_status="Pending"
                your_complaint_no=your_complaint_no
                print("")
                sql="insert into clean (complaint, complaint_area, your_name, mobile_no,r_date , your_status, your_complaint_no) values(%s,%s,%s,%s,%s,%s,%s)"
                c.execute(sql,(complaint, complaint_area, your_name, mobile_no, r_date,your_status, your_complaint_no,))
                print("")

                state3=True

                while state3==True:
                    captcha1=random.randint(0,10000)
                    print("Verify that u r not A ROBOT!")
                    print(captcha1)
                    rcaptcha1=eval(input("Enter the captcha seen:"))

                    if rcaptcha1==captcha1:
                        print("Pass!") 
                        print("")
                        state3=False

                    else:
                        print("Retry!")
                        print("")
            print("Your complaint no. is:", your_complaint_no)
            mydb.commit()

        elif OPTION2=="s1" or OPTION2=="S1":
            def status():
                print("")
                COMPLAINT_CODE2=input("Enter your compliantno:")
                c.execute("select your_status from clean where your_complaint_no=%s",(COMPLAINT_CODE2,))
                records = c.fetchall()
                print("Complaint status: ",records[0][0])
            status()
#End of table 2

    print("Press any key to continue...")
    print("....................................................................................")
    you=input("")
    os.system('cls') # Clear output window
