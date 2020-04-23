from tkinter import *
from functools import partial
import connection
import PIL
from PIL import ImageTk
from PIL import Image

v = " "
sql = " "

newTab = Tk() 
newTab.title("Administrator bar")
newTab.geometry("500x500")



def chooseFrom(value):
  global newTab
  v = value.get()
  
  if v=='products':
    products_page = Tk()
    products_page.title("Product info")
    products_page.geometry("700x500")
    
    select_all = connection.cur.execute("select * from bj_products").fetchall()    
    column_name = [row[0] for row in connection.cur.description]
    for j in range(len(column_name)):
      column_names = Label(products_page,text =column_name[j] ).grid(row = 0, column = j)
      for i  in range(len(select_all)):
        res = Label(products_page,text = select_all[i][j]).grid(row = i+1, column = j)
    end_inc = i+2

    productAddLabel1 = Label(products_page,text = "Product ID").grid(row = end_inc, column = 0)
    add_prod_id = StringVar(products_page)
    l3 = Entry(products_page,textvariable=add_prod_id).grid(row=end_inc,column=1)
    end_inc+=1
    productAddLabel2 = Label(products_page,text = "Product Name").grid(row = end_inc, column = 0)
    add_prod_name = StringVar(products_page)
    l3 = Entry(products_page,textvariable=add_prod_name).grid(row=end_inc,column=1)
    end_inc+=1
    productAddLabel3 = Label(products_page,text = "Product Price").grid(row = end_inc, column = 0)
    add_prod_price = StringVar(products_page)
    l3 = Entry(products_page,textvariable=add_prod_price).grid(row=end_inc,column=1)
    end_inc+=1
    productAddLabel4 = Label(products_page,text = "Product Receipt").grid(row = end_inc, column = 0)
    add_prod_rec = StringVar(products_page)
    l3 = Entry(products_page,textvariable=add_prod_rec).grid(row=end_inc,column=1)
    end_inc+=1
    productAddLabel5 = Label(products_page,text = "Product Ingredients").grid(row = end_inc, column = 0)
    add_prod_ingr = StringVar(products_page)
    l3 = Entry(products_page,textvariable=add_prod_ingr).grid(row=end_inc,column=1)
    end_inc+=1
    productAddLabel6 = Label(products_page,text = "Product calories").grid(row = end_inc, column = 0)
    add_prod_cal = StringVar(products_page)
    l3 = Entry(products_page,textvariable=add_prod_cal).grid(row=end_inc,column=1)
    end_inc+=1
    productAddLabel7 = Label(products_page,text = "Product Type").grid(row = end_inc, column = 0)
    add_prod_type = StringVar(products_page)
    l3 = Entry(products_page,textvariable=add_prod_type).grid(row=end_inc,column=1)
    end_inc+=1

    global add_product
    add_product = partial(add_product,add_prod_id,add_prod_name,add_prod_price,add_prod_rec,add_prod_ingr,add_prod_cal,add_prod_type)
    addButton = Button(products_page,text="add", command=add_product).grid(row =end_inc+1,column =1)  


    productDeleteLabel = Label(products_page,text = "Delete by ID").grid(row = i+2, column = 2)
    del_prod = StringVar(products_page)
    dLabel = Entry(products_page,textvariable=del_prod).grid(row=i+2,column=3)

    global del_product
    del_product = partial(del_product,del_prod)
    delButton = Button(products_page,text="delete", command=del_product).grid(row =i+2,column =4)  
    
  elif v=='schedule':
    schedule_page = Tk()
    schedule_page.title("Schedule info")
    schedule_page.geometry("400x100")

    var = StringVar(schedule_page)
    var.set("28.03.2020-5.04.2020")
    w2 = OptionMenu(schedule_page,var,"28.03.2020-5.04.2020","5.04.2020-12.04.2020","12.04.2020-19.04.2020").grid(row=0,column=1)
    lb1 = Label(schedule_page,text = "Choose which week's schedule you want to see: ").grid(row = 0, column =0)

    #img = Image.open("new.jpg")
    #label = Label(schedule_page,image=img)
    
  else:
    pass
#below is employees part functionality
def find_by_id(input_id):
  sql = input_id.get()
  search_page = Tk()
  search_page.title("Result info")
  search_page.geometry("800x50")
  query = connection.cur.execute("select * from bj_employees where employee_id="+sql).fetchone()
  col = [row[0] for row in connection.cur.description]
  #print(col)
  for i in range(len(col)):
    column_names = Label(search_page,text =col[i] ).grid(row = 0, column =i)
    res = Label(search_page,text = query[i]).grid(row = 1, column =i)


def del_by_id(input_id):
  sql = input_id.get()
  del_page = Tk()
  del_page.title("Result info")
  del_page.geometry("500x100")
  query = connection.cur.execute("delete from bj_employees where employee_id="+sql)
  res = Label(del_page,text = "Deleted Successfully!").grid(row = 0, column =0)
  connection.connection.commit()

def add_user(add_emp_id,add_first_name,add_last_name,add_email,add_phone,add_hire_date,add_job_id,add_job_pass,add_salary,add_man_id):
  emp_id = add_emp_id.get()
  first_name = add_first_name.get()
  last_name = add_last_name.get()
  email = add_email.get()
  phone = add_phone.get()
  hire_date = add_hire_date.get()
  job_id = add_job_id.get()
  job_pass = add_job_pass.get()
  salary = add_salary.get()
  man_id = add_man_id.get()
  query = connection.cur.execute("insert into bj_employees values({},'{}','{}','{}','{}','{}','{}','{}',{},{})".format(emp_id,first_name,last_name,email,phone,hire_date,job_id,job_pass,salary,man_id))  
  connection.connection.commit()
#end og employees part functionality


#below is products part functionality
def add_product(add_prod_id,add_prod_name,add_prod_price,add_prod_rec,add_prod_ingr,add_prod_cal,add_prod_type):
  prod_id = add_prod_id.get()
  prod_name = add_prod_name.get()
  price = add_prod_price.get()
  rec = add_prod_rec.get()
  ingr = add_prod_ingr.get()
  cal = add_prod_cal.get()
  prod_type = add_prod_type.get()
  query = connection.cur.execute("insert into bj_products values({},'{}',{},'{}','{}','{}','{}')".format(prod_id,prod_name,price,rec,ingr,cal,prod_type))  
  connection.connection.commit()  

def del_product(del_prod):
  prod_id = del_prod.get()
  query = connection.cur.execute("delete from bj_products where product_id="+prod_id)  
  connection.connection.commit()  

#end of products part functionaluity

def getAllInfo():
  info = Tk()
  info.geometry("600x600")
  info.title("Summary information about employees")


  query1 = connection.cur.execute("select first_name, last_name,salary from bj_employees order by job_id").fetchall()
  column_name = [row[0] for row in connection.cur.description]
  for j in range(len(column_name)):
    column_names = Label(info,text =column_name[j] ).grid(row = 0, column = j)
  for j in range(len(query1)):
    for i in range(len(query1[j])):
      lbl1 = Label(info, text = query1[j][i]).grid(row=j+1,column=i)
  query2 = connection.cur.execute("select job_id,(sum(extract( minute from bj_clock_in.end_time - bj_clock_in.start_time))/60) as Hours FROM bj_clock_in group by job_id order by job_id").fetchall()
  column_name = [row[0] for row in connection.cur.description]
  for j in range(len(column_name)):
    column_names = Label(info,text =column_name[j] ).grid(row = 0, column = j+3)
  for m in range(len(query2)):
    for n in range(len(query2[m])):
      lbl2 = Label(info, text = query2[m][n]).grid(row=m+1,column=i+n+1)
  for l in range(len(query1)):
    lbl3 = Label(info,text= round(query1[l][2]*query2[l][1])).grid(row=l+1,column=5)
  lbl4 = Label(info,text= "Total pay check amount").grid(row=0,column=5)  
v = "employees"

addLabel2 = Label(newTab,text=v,bg="green").grid(row=2,column=1)
deleteLabel2 = Label(newTab,text=v,bg="red").grid(row=14,column=1)
findLabel2 = Label(newTab,text=v,bg="blue").grid(row=16,column=1)
variable = StringVar(newTab)
variable.set(v)
    
userIdLabel = Label(newTab, text = "Manage").grid(row=0,column=0)

w = OptionMenu(newTab,variable,"employees","products","schedule")
w.grid(row=0,column=1)
    
chooseFrom = partial(chooseFrom,variable)
chooseButton = Button(newTab, text="choose", command = chooseFrom).grid(row=0,column=2)

#add or update works here
addLabel = Label(newTab,text="Add",bg="green").grid(row=2,column = 0)


add_emp_id = StringVar(newTab)
add_first_name = StringVar(newTab)
add_last_name = StringVar(newTab)
add_email = StringVar(newTab)
add_phone = StringVar(newTab)
add_hire_date = StringVar(newTab)
add_job_id = StringVar(newTab)
add_job_pass = StringVar(newTab)
add_salary = StringVar(newTab)
add_man_id = StringVar(newTab)

addLabel3 = Label(newTab,text="Employee ID").grid(row=3,column=0)
l3 = Entry(newTab,textvariable=add_emp_id).grid(row=3,column=1)
addLabel4 = Label(newTab,text="First Name").grid(row=4,column=0)
l4 = Entry(newTab, textvariable=add_first_name).grid(row=4,column=1)
addLabel5 = Label(newTab,text="Last Name").grid(row=5,column=0)
l5 = Entry(newTab, textvariable=add_last_name).grid(row=5,column=1)
addLabel6 = Label(newTab,text="Email").grid(row=6,column = 0)
l6 = Entry(newTab, textvariable=add_email).grid(row=6, column=1)
addLabel7 = Label(newTab,text="Phone number").grid(row=7,column = 0)
l7 = Entry(newTab, textvariable=add_phone).grid(row=7, column=1)
addLabel8 = Label(newTab,text="Hire date").grid(row=8,column = 0)
l8 = Entry(newTab, textvariable=add_hire_date).grid(row=8, column=1)
addLabel9 = Label(newTab,text="Job ID").grid(row=9,column = 0)
l9 = Entry(newTab, textvariable=add_job_id).grid(row=9, column=1)
addLabel10 = Label(newTab,text="Job password").grid(row=10,column = 0)
l10 = Entry(newTab, textvariable=add_job_pass).grid(row=10, column=1)
addLabel11 = Label(newTab,text="Salary").grid(row=11,column = 0)
l11 = Entry(newTab, textvariable=add_salary).grid(row=11, column=1)
addLabel12 = Label(newTab,text="Manager ID").grid(row=12,column = 0)
l12 = Entry(newTab, textvariable=add_man_id).grid(row=12, column=1)


add_user = partial(add_user,add_emp_id,add_first_name,add_last_name,add_email,add_phone,add_hire_date,add_job_id,add_job_pass,add_salary,add_man_id)
addButton = Button(newTab,text="add", command=add_user).grid(row =12,column =2)

#Delete works here
did = Label(newTab,text = "ID").grid(row=15,column=0)
deleteLabel = Label(newTab,text="Delete",bg="red").grid(row=14,column=0)
del_id = StringVar(newTab)
deleteLabel = Entry(newTab,textvariable=del_id).grid(row=15,column =1)
del_by_id = partial(del_by_id,del_id)
delButton = Button(newTab, text="delete", command=del_by_id).grid(row=15, column=2)  

        
#Find works here
fid = Label(newTab,text = "ID").grid(row=17,column=0)
findLabel = Label(newTab,text="Find",bg="blue").grid(row=16,column= 0)
str_id = StringVar(newTab)
findLabel = Entry(newTab,textvariable=str_id).grid(row=17,column =1)
find_by_id = partial(find_by_id, str_id)
findButton = Button(newTab, text="search", command=find_by_id).grid(row=17, column=2)  
# get all information works here
getAllInfoButton = Button(newTab, text="get All information", command=getAllInfo).grid(row=19, column=1)  


newTab.mainloop()



    
