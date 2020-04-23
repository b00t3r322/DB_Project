from tkinter import *
from functools import partial
import connection
import time

root = Tk()
root.title("Ben & Jerry's")
root.geometry("150x150")

access_allowed = dict()
auth_data = []
emp_table = connection.cur.execute('select * from bj_employees')
for line in emp_table.fetchall():
  access_allowed[line[6]] = line[7]

def validateLogin(userid, password):
        if userid.get() in access_allowed and password.get()==access_allowed[userid.get()]:
            myLabel1 = Label(root,text="Welcome!!!").grid(row = 5,column =1)
            if userid.get()=='0001':
              root.destroy()
              exec(open('./addminpage.py').read())  
            else:
              root.destroy()
              t = time.localtime()
              date_time = time.strftime("%Y/%m/%d, %H:%M:%S",t)      
              connection.cur.execute("insert into bj_clock_in values({},to_timestamp('{}' , 'YYYY-MM-DD HH24:MI:SS'),to_timestamp('2021-04-20', 'YYYY-MM-DD HH24:MI:SS'))".format(userid.get(),date_time))
              connection.connection.commit()
              exec(open('./userpage.py').read())              
        else:
            myLabel2 = Label(root,text="Incorrect credntials. Try again, please").grid(row = 5,column =1)

    

userIdLabel = Label(root, text = "User ID").grid(row=0,column=1)
userid = StringVar()
userIdEntry = Entry(root, textvariable=userid).grid(row=1, column=1)

passwordLabel = Label(root,text="Password").grid(row=2, column=1)  
password = StringVar()
passwordEntry = Entry(root, textvariable=password, show='*').grid(row=3, column=1)  


validateLogin = partial(validateLogin, userid, password)


#login button
loginButton = Button(root, text="Login", command=validateLogin).grid(row=4, column=1)  

root.mainloop()