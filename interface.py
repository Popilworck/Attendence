import mysql.connector,os,csv
from datetime import date
password='2560'#enter password here
def onest():
        conn1 = mysql.connector.connect(username='root',host='localhost',password=password,database = 'world')
        conn1.autocommit = True
        c1 = conn1.cursor()
        c1.execute('create database if not exists attendence;')
conn = mysql.connector.connect(host = 'localhost',user = 'root',password=password,database = 'attendence')
c = conn.cursor()
conn.autocommit = True
l=os.getcwd()
def getdiv(a):
    c.execute(f'select divs from structure where grade={a}')
    return(list(c.fetchall()[0][0]))
def getatt(g,d,m):
    q=f'select * from {m} where grade = {g} and division = "{d}"'
    c.execute(q)
    x=[i[1:] for i in  c.fetchall()]
    return(x)
def getid(table):
    q=f'Select max(id) from {table}'
    c.execute(q)
    return(c.fetchone()[0])
def getname(i):
    q=f'Select name from student where id = {i}'
    c.execute(q)
    return(c.fetchone()[0])
def getnames(g,d):
    q=f'select name from student where grade = {g} and division = "{d}"'
    c.execute(q)
    return(c.fetchall())
def addatt(g,d,day,m,attlist):
    for key,value in attlist.items():
        q=f'update {m} set _{day} = "{value}" where grade = {g} and name = "{key}" and division = {d}'
        c.execute(q)
if __name__ == '__main__':
    onest()
