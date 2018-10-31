from psql_helper import PsqlHelper
import os 
from conf import *
def class Students(object):
    def __init__(self):
        self.db=PsqlHelper(db_name)
    def CreateTable(self):
        sql='CREATE TABLE Students (name varchar(80),age int);'
        params=()
        self.db.ModifyTableOne(sql,params)
    def DeleteTable(self):
        sql='DROP TABLE Students;'
        params=()
        self.db.ModifyTableOne(sql,params)
    def AddStudent(self,name,age):
        sql='INSERT INTO Students VALUES(%s,%d);'
        params=(name,age,)
        self.db.ModifyTableOne(sql,params)
    def DeleteStudent(self,name):
        sql='DELETE FROM Students WHERE name=s%;'
        params=(name,)
    def EditAge(self,name,age):
        sql='UPDATE Students SET age=%d WHERE name=%s;'
        params=(age,name,)
        self.db.ModifyTableOne(sql,params)
    def GetStudentInfo(self,name):
        sql='SELECT * FROM Students WHERE name=s%;'
        params=(name,)
        student_info=self.db.GetDataOne(sql,params)
        print("Name:s%  Age:d%"%(student_info['name'],student_info['age']))
    def GetAllStudents(self):
        sql='SELECT * FROM Students;'
        params=()
        all_students=self.db.GetDataDict(sql,params)
        for student in all_students:
            print("Name:s%  Age:d%"%(student_info['name'],student_info['age'])) 

cmd='PGPASSWORD=s% createdb -h %s -U %s -p %s s%'%(password,db_ip,username,db_port,db_name)
os.sys(cmd)