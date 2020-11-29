import mysql.connector
from dbConnect import DBConnect

hostname = 'freedb.tech'
MYSQLusername = 'freedbtech_Aniket'
MYSQLpass = 'Aniket@2000'
dbname = 'freedbtech_RMS'



def selectall():
    mydb=mysql.connector.connect(host=hostname,user=MYSQLusername,password=MYSQLpass,database=dbname,port='3306')
    mycursor=mydb.cursor()
    query = ("SELECT ID, fname, lname, Role, exp, salary, att_today, att_total FROM workers")
    mycursor.execute(query)
    for(ID, fname, lname, Role, exp, salary, att_today, att_total) in mycursor:
        s="{}   {}   {}   {}   {}   {}   {}   {}".format(ID, fname, lname, Role, exp, salary, att_today, att_total)
        print(s)


def insert(fname1, lname1, Role1, exp1, salary1, att_today1, att_total1):
    '''
    fname1 --> str
    lname1 --> str
    Role1 --> str
    exp1 --> int
    salary1 --> integer
    att_today1 --> integer
    att_total1 --> integer
    '''
    database = DBConnect(host=hostname,user=MYSQLusername,password=MYSQLpass, database=dbname)
    new_user = {'fname' : fname1, 'lname' : lname1, 'Role' : Role1, 'exp' : exp1,
                'salary' : salary1, 'att_today' : att_today1, 'att_total' : att_total1}
    database.insert(new_user,'workers')
    database.commit()

def deleterow(id1):
    '''
    id1 --> integer
    '''
    mydb=mysql.connector.connect(host=hostname,user=MYSQLusername,password=MYSQLpass,database=dbname,port='3306')
    mycursor=mydb.cursor()
    query=("DELETE FROM workers WHERE ID = %s" %(id1))
    mycursor.execute(query)
    mydb.commit()


def today_attend_submit(id1):
    '''
    id1 --> integer
    '''
    mydb=mysql.connector.connect(host=hostname,user=MYSQLusername,password=MYSQLpass,database=dbname,port='3306')
    mycursor=mydb.cursor()
    query=("UPDATE workers set att_today = %s WHERE ID = %s" %(1,id1))
    mycursor.execute(query)
    mydb.commit()

def reset_today_attend():
    mydb=mysql.connector.connect(host=hostname,user=MYSQLusername,password=MYSQLpass,database=dbname,port='3306')
    mycursor=mydb.cursor()
    query=("UPDATE workers set att_today = 0")
    mycursor.execute(query)
    mydb.commit()

def update_total_attend():
    mydb=mysql.connector.connect(host=hostname,user=MYSQLusername,password=MYSQLpass,database=dbname,port='3306')
    mycursor=mydb.cursor()
    query=("UPDATE workers set att_total = att_total + 1 WHERE att_today = 1")
    mycursor.execute(query)
    mydb.commit()

def reset_total_attend():
    mydb=mysql.connector.connect(host=hostname,user=MYSQLusername,password=MYSQLpass,database=dbname,port='3306')
    mycursor=mydb.cursor()
    query=("UPDATE workers set att_total = 0")
    mycursor.execute(query)
    mydb.commit()

 # ID, fname, lname, Role, exp, salary, att_today, att_total
insert("testf1","testf1",'Tester',2,50000,0,0)
insert("testf2","testf2",'Tester',2,50000,0,0)
insert("testf3","testf3",'Tester',2,50000,0,0)
insert("testf4","testf4",'Tester',2,50000,0,0)
print("###################### insert test passed ##############################")

selectall()
print("###################### select test passed ##############################")

id_to_delete = int(input("Enter the ID that you want to delete"))
deleterow(id_to_delete)
print("###################### delete test passed ##############################")

selectall()
id_to_delete = int(input("Enter the ID that you want to update"))
today_attend_submit(id_to_delete)
selectall()
print("###################### today_attend_submit test passed ##############################")

update_total_attend()
selectall()
print("###################### update_total_attend test passed ##############################")

reset_today_attend()
selectall()
print("###################### reset_today_attend test passed ##############################")

reset_total_attend()
selectall()
print("###################### reset_total_attend test passed ##############################")
