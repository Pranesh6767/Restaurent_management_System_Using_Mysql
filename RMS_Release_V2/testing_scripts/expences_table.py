import mysql.connector
from dbConnect import DBConnect

hostname = 'freedb.tech'
MYSQLusername = 'freedbtech_Aniket'
MYSQLpass = 'Aniket@2000'
dbname = 'freedbtech_RMS'



def selectall():
    mydb=mysql.connector.connect(host=hostname,user=MYSQLusername,password=MYSQLpass,database=dbname,port='3306')
    mycursor=mydb.cursor()
    query = ("SELECT ID, year, month, day, type, ammount FROM Expences")
    mycursor.execute(query)
    for(ID, year, month, day, type, ammount) in mycursor:
        s="{}   {}   {}   {}   {}   {}".format(ID, year, month, day, type, ammount)
        print(s)


def insert(year1,month1,day1,type1,ammount1):
    '''
    year1 --> integer
    month1 --> integer
    day1 --> integer
    type1 --> str
    ammount1 --> integer
    '''
    database = DBConnect(host=hostname,user=MYSQLusername,password=MYSQLpass, database=dbname)
    new_user = {'year': year1,'month': month1,'day': day1,'type': type1,'ammount': ammount1}
    database.insert(new_user,'Expences')
    database.commit()

def deleterow(id1):
    mydb=mysql.connector.connect(host=hostname,user=MYSQLusername,password=MYSQLpass,database=dbname,port='3306')
    mycursor=mydb.cursor()
    query=("DELETE FROM Expences WHERE ID = %s" %(id1))
    mycursor.execute(query)
    mydb.commit()

def sumofall():
    mydb=mysql.connector.connect(host=hostname,user=MYSQLusername,password=MYSQLpass,database=dbname,port='3306')
    mycursor=mydb.cursor()
    query = ("SELECT sum(ammount) from Expences")
    mycursor.execute(query)
    for(ammount) in mycursor:
        total_expences = int(ammount[0])
    print(total_expences)


insert(2016,6,16,"testing module test4",2000)
insert(2016,6,17,"testing module test5",2000)
insert(2016,6,18,"testing module test6",2000)
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
