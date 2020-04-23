from tkinter import *
from functools import partial
import connection
import time

def end_shift(user_id,start_time):
  global newTab
  t = time.localtime()
  date_time = time.strftime("%Y/%m/%d, %H:%M:%S",t) 
  print(date_time,user_id,start_time)    
  query = connection.cur.execute("UPDATE bj_clock_in SET end_time = to_timestamp('{}' , 'YYYY-MM-DD HH24:MI:SS') where job_id = '{}'  and start_time = to_timestamp('{}', 'YYYY-MM-DD HH24:MI:SS')".format(date_time,user_id, start_time))
  connection.connection.commit()
  print("Done Updated")
  newTab.destroy()

newTab = Tk() 
newTab.title("User bar")
newTab.geometry("500x300")

user = connection.cur.execute("select job_id,start_time from bj_clock_in order by start_time desc ").fetchone()
user_id = user[0]
start_time = user[1]

name = connection.cur.execute("select first_name from bj_employees where job_id="+str(user_id)).fetchone()

lbl2 = Label(newTab, text = "Shift started at: ").grid(row = 0, column = 3)
lbl1 = Label(newTab, text = "Welcome,").grid(row = 0, column = 1)
lbl3 = Label(newTab, text = name).grid(row = 0, column = 2)
lbl4 = Label(newTab, text = start_time).grid(row = 0, column = 4)

end_shift = partial(end_shift,user_id,start_time)
delButton = Button(newTab,text="End shift", command=end_shift).grid(row =0,column =5)
