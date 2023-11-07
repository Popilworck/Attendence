import mysql.connector,calendar, names,random,interface
from datetime import date
password='lab@2022'#put password here
conn = mysql.connector.connect(host = 'localhost',user = 'root',password=password,database = 'attendence')
c = conn.cursor()
conn.autocommit = True
months = [i for i in calendar.month_name][1:]
def startup():#creates tables
    for j in months:
        f='(id int primary key, name varchar(255),grade int, division char(1),'
        for i in range(1,calendar.monthrange(int(str(date.today())[:4]),months.index(j)+1)[1]+1):
            f+=f'_{str(i)} char(1) default "",'
        f+='foreign key (id) references student(id));'
        q=f'create table {j}{f}'
        c.execute(q)

def insert(g):#inserts info into tables
    for j in months:
        id_max = interface.getid(j) if interface.getid(j) != None else 0
        for i in range(1,21):
            p_list = random.choices(['A','P','H'],weights=(20,100,1),k=calendar.monthrange(int(str(date.today())[:4]),months.index(j)+1)[1])
            p_list_str = ''
            for q in p_list:p_list_str+=f'"{q}",'
            p_list_str=p_list_str[:-1]
            d=random.choice(('A','B',"C"))
            q= f'insert into {j.lower()} values ({id_max+1},"{interface.getname(id_max+1)}",{g},"{d}",{p_list_str})'
            print(q)
            id_max+=1
            c.execute(q)

def new_student(n,g,d):#creates new studnets
    id_max  = interface.getid('Student')
    q=f'insert into student values({id_max+1},"{n}",{g},"{d}")'
    c.execute(q)
#for i in range(1000):#creates 1000 new students
   # new_student(names.get_full_name(),random.choice(range(1,13)),random.choice(('A',"B","C")))
#for i in range(1,13):# inserts data into table
   #insert(i)
def truncate():#clears all tables
    for i in months:
        c.execute(f'truncate table {i};')
#truncate
def onest():#creates database
        conn1 = mysql.connector.connect(username='root',host='localhost',password=password,database = 'world')
        conn1.autocommit = True
        c1 = conn1.cursor()
        c1.execute('create database if not exists attendence;')
