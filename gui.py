from tkinter import *
from PIL import Image,ImageTk
from datetime import date
import calendar
from tkinter import ttk,messagebox
import interface
window = Tk()
x= lambda:messagebox.showerror("ERROR", "INVALID INPUT, PLEASE RE-ENTER")
o = lambda a: a/1536
p= lambda a:a/888
fonts = lambda a:("Inter ExtraBold", a * -1,'bold')
def clearwindow():
        for i in window.winfo_children():
            i.destroy()
months = [i for i in calendar.month_name][1:]
def window1():
    clearwindow()
    tks_logo =  ImageTk.PhotoImage(Image.open('tkslogo.jpeg'))
    tks = Label(window,image=tks_logo)
    tks.place(relx=0,rely=0)
    tks.image = tks_logo
    Label(window,text="STUDENT ATTENDENCE MANAGEMENT",font=fonts(52)).place(relx=0.2,rely=0.1)
    Label(window,text="CHOOSE GRADE, DIVISION & MONTH",font=fonts(32)).place(relx=o(400),rely=p(300))
    grade_list=[f'Grade {i}' for i in range(1,13)]
    grade_var = StringVar()
    box = ttk.Combobox(window,values=grade_list,textvariable=grade_var,font=fonts(21))
    box.place(relx=o(600),rely=p(400),relheight=p(30))
    Label(window,text="Grade",font=fonts(21)).place(relx=o(500),rely=p(400))
    def submit1():
        try:
            submit(int(grade_var.get()[6:]))  
            sub_button1.destroy()
        except:x()
    def submit(grade):
        def sub2():
            if messagebox.askyesno("View Attendece",'Do you want to view attendence?'):
                try:window3(grade,div_var.get(),month.get())
                except:x()
            else:
               if messagebox.askyesno("Add Attendence","Do you want to add attendence?"):
                   try:window2(grade,div_var.get(),month.get())
                   except:x()
        div_var=StringVar()
        m = [i for i in calendar.month_name][1:]
        month = StringVar()
        div_list= interface.getdiv(grade)
        box2 =ttk.Combobox(window,values=div_list,textvariable=div_var)
        box2.place(relx=o(600),relheight=p(30),rely=(p(500)))
        Label(window,text="Division",font=fonts(21)).place(relx=o(500),rely=p(500))
        box3= ttk.Combobox(window,values=m,textvariable=month)
        box3.place(relx=o(600),relheight=p(30),rely=p(600))
        Label(window,text="Month",font=fonts(21)).place(relx=o(500),rely=p(600))
        Button(window,text='Submit',font=fonts(21),command= lambda : sub2()).place(relx=o(650),rely=p(700))
    sub_button1 = Button(window,text='Submit',font=fonts(21),command=submit1)
    sub_button1.place(relx=o(650),rely=p(750))
window1()
def window3(g,d,m):
    clearwindow()
    #print(g)
    table = ttk.Treeview(window)
    days = calendar.monthrange(int(str(date.today())[:4]),months.index(m)+1)[1]
    f=''
    for i in range(1,days+1):f+=f',"_{i}"'
    exec(f"table['columns'] = ('Name','Grade','Division' {f})") 
    table.column('#0',width=0,stretch=0)
    table.column('Name',width=100)
    table.column('Grade',width=20)
    table.column('Division',width=22)
    table.heading('#0',text='')
    for i in ['Name',"Grade","Division"]:
        table.heading(i,text=i)
    for i in range(1,days+1):
        table.column(f'_{i}',width=20,anchor='center')
        table.heading(column=f'_{i}',text=f'{i}')
    table.place(relx=0,rely=0.04,relheight=0.96,relwidth=0.99)
    for i in interface.getatt(g,d,m):
        table.insert(parent='',values=i,index='end')
    sb = Scrollbar(window,orient='vertical')
    table.yview_scroll=sb
    sb.place(relx=0.99,rely=0.1,relheight=0.96)
    Button(window,command=window1,text="Back").place(relx=0,rely=0,relheight=0.04,width=70)
def window2(g,d,m):
    def sub():
        day = int(entry1.get())
        if 0<day<=31:
            clearwindow()
            att={}
            names = interface.getnames(g,d)
            for i in names:
                att[i[0]]= 'P' if messagebox.askyesno("Add Attendence",f'Was {i[0]} Present?') else 'A'
            messagebox.showinfo("Attendence Recorded","Attendence Succesfully Recorded")
            interface.addatt(g,d,day,m,att)
            window1()
        else: x()
    clearwindow()
    Label(window,text='Enter Date (dd)',font=fonts(32)).place(relx=o(500),rely=p(130))
    entry1=Entry(window,font=fonts(21))
    entry1.place(relx=o(500),rely=p(200))
    Button(window,text="SUBMIT",command= sub).place(relx=o(500),rely=p(300))
window.attributes('-fullscreen',True)
window.bind('<Escape>',lambda a: window.destroy())
window.bind('<Return>',lambda a:window2(12,'A','July'))
window.mainloop()