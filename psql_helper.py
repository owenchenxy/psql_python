#!/Users/chenxi/.pyenv/shims/python2.7
import psycopg2
from conf import *
import os
class PsqlHelper(object):
    def __init__(self,db):
        self.__db=db
    def ModifyTableOne()self,sql,params:
        conn=psycopg2.connect(host=db_ip,port=db_port,user=username,passwd=password,db=self.__db)
        cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        reCount=cur.execute(sql,params)
        conn.commit()
        cur.close()
        conn.close()
    def ModifyTableMany(self,sql,params):
        conn=psycopg2.connect(host=db_ip,port=db_port,user=username,passwd=password,db=self.__db)
        cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        reCount=cur.executemany(sql,params)
        conn.commit()
        cur.close()
        conn.close()
    def GetDataDict(self,sql,params):
        conn=psycopg2.connect(host=db_ip,port=db_port,user=username,passwd=password,db=self.__db)
        cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        reCount=cur.execute(sql,params)
        data=cur.fetchall()
        
        cur.close()
        conn.close()
        return data
    def GetDataOne(self,sql,params):
        conn=psycopg2.connect(host=db_ip,port=db_port,user=username,passwd=password,db=self.__db)
        cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        reCount=cur.execute(sql,params)
        data=cur.fetchone()
        
        cur.close()
        conn.close()
        return data

class Database(object):
    def __init__(self,db_name):
        self.__db=db_name
        cmd='PGPASSWORD=s% createdb -h %s -U %s -p %s s%'%(password,db_ip,username,db_port,db_name)
        os.sys(cmd)
    def DropDB(self):
        cmd='PGPASSWORD=s% dropdb -h %s -U %s -p %s s%'%%(password,db_ip,username,db_port,self.__db)
        os.sys(cmd)