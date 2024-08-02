from tkinter import Tk
from tkinter import Label
import datetime
def date_time():
    time = datetime.datetime.now()
    hr = time.strftime('%I')
    mi = time.strftime('%M')
    sec = time.strftime('%S')
    am = time.strftime('%p')
    date = time.strftime("%d")
    month = time.strftime("%m")
    year = time.strftime("%y")
    day = time.strftime("%a")


    Lab_hr.config(text=hr)
    Lab_min.config(text=mi)
    Lab_sec.config(text=sec)
    Lab_am.config(text=am)

    Lab_date.config(text=date)
    Lab_mo.config(text=month)
    Lab_year.config(text=year)
    Lab_day.config(text=day)

    Lab_hr.after(200,date_time)


root = Tk()
root.title('  ****Digital clock****  ')
root.geometry('1000x500')
root.config(bg='black')

# time

Lab_hr = Label(root,text="00",font=('Time New Roman',30,"bold"),bg="red",fg="white")
Lab_hr.place(x=120,y=50,height=110,width=100)

Lab_hr_txt = Label(root,text="Hour",font=('Time New Roman',20,"bold"),bg="red",fg="white")
Lab_hr_txt.place(x=120,y=190,height=40,width=100)

Lab_min = Label(root,text="00",font=('Time New Roman',30,"bold"),bg="red",fg="white")
Lab_min.place(x=340,y=50,height=110,width=100)

Lab_min_txt = Label(root,text="Min.",font=('Time New Roman',20,"bold"),bg="red",fg="white")
Lab_min_txt.place(x=340,y=190,height=40,width=100)

Lab_sec = Label(root,text="00",font=('Time New Roman',30,"bold"),bg="red",fg="white")
Lab_sec.place(x=560,y=50,height=110,width=100)

Lab_sec_txt = Label(root,text="Sec.",font=('Time New Roman',20,"bold"),bg="red",fg="white")
Lab_sec_txt.place(x=560,y=190,height=40,width=100)

Lab_am = Label(root,text="00",font=('Time New Roman',30,"bold"),bg="red",fg="white")
Lab_am.place(x=780,y=50,height=110,width=100)

Lab_am_txt = Label(root,text="AM/PM",font=('Time New Roman',20,"bold"),bg="red",fg="white")
Lab_am_txt.place(x=780,y=190,height=40,width=100)

#  date

Lab_date = Label(root,text="00",font=('Time New Roman',30,"bold"),bg="red",fg="white")
Lab_date.place(x=120,y=270,height=110,width=100)

Lab_date_txt = Label(root,text="date",font=('Time New Roman',20,"bold"),bg="red",fg="white")
Lab_date_txt.place(x=120,y=410,height=40,width=100)

Lab_mo = Label(root,text="00",font=('Time New Roman',30,"bold"),bg="red",fg="white")
Lab_mo.place(x=340,y=270,height=110,width=100)

Lab_mo_txt = Label(root,text="Month",font=('Time New Roman',20,"bold"),bg="red",fg="white")
Lab_mo_txt.place(x=340,y=410,height=40,width=100)

Lab_year= Label(root,text="00",font=('Time New Roman',30,"bold"),bg="red",fg="white")
Lab_year.place(x=560,y=270,height=110,width=100)

Lab_year_txt = Label(root,text="year",font=('Time New Roman',20,"bold"),bg="red",fg="white")
Lab_year_txt.place(x=560,y=410,height=40,width=100)

Lab_day = Label(root,text="00",font=('Time New Roman',30,"bold"),bg="red",fg="white")
Lab_day.place(x=780,y=270,height=110,width=100)

Lab_day_txt = Label(root,text="Day",font=('Time New Roman',20,"bold"),bg="red",fg="white")
Lab_day_txt.place(x=780,y=410,height=40,width=100)


date_time()

root.mainloop()



