import mysql.connector
from dbConnect import DBConnect

hostname = 'freedb.tech'
MYSQLusername = 'freedbtech_Aniket'
MYSQLpass = 'Aniket@2000'
dbname = 'freedbtech_RMS'



def selectall():
    mydb=mysql.connector.connect(host=hostname,user=MYSQLusername,password=MYSQLpass,database=dbname,port='3306')
    mycursor=mydb.cursor()
    query = ("SELECT ID, type, ammount FROM Maintainance")
    mycursor.execute(query)
    for(ID, type, ammount) in mycursor:
        s="{}   {}   {}".format(ID, type, ammount)
        print(s)


def insert(type1,ammount1):
    '''
    type1 --> str
    ammount1 --> integer
    '''
    database = DBConnect(host=hostname,user=MYSQLusername,password=MYSQLpass, database=dbname)
    new_user = {'type': type1,'ammount': ammount1}
    database.insert(new_user,'Maintainance')
    database.commit()

def deleterow(id1):
    '''
    id --> integer
    '''
    mydb=mysql.connector.connect(host=hostname,user=MYSQLusername,password=MYSQLpass,database=dbname,port='3306')
    mycursor=mydb.cursor()
    query=("DELETE FROM Maintainance WHERE ID = %s" %(id1))
    mycursor.execute(query)
    mydb.commit()

def sumofall():
    mydb=mysql.connector.connect(host=hostname,user=MYSQLusername,password=MYSQLpass,database=dbname,port='3306')
    mycursor=mydb.cursor()
    query = ("SELECT sum(ammount) from Maintainance")
    mycursor.execute(query)
    for(ammount) in mycursor:
        total_expences = int(ammount[0])
    print(total_expences)


insert("testing module test7",3000)
insert("testing module test8",3000)
insert("testing module test9",3000)
print("###################### insert test passed ##############################")
selectall()
print("###################### select test passed ##############################")
id_to_delete = int(input("Enter the ID that you want to delete"))
deleterow(id_to_delete)
print("###################### delete test passed ##############################")
sumofall()
print("###################### SUM test passed ##############################")
selectall()
print("###################### final results ##############################")
