import tkinter as tk
from tkinter import *

# ------------------- W I N D O W -------------------
r = tk.Tk()
r.geometry("800x400")
r.title("Google Clone")
r.iconbitmap("C:/Users/robin/OneDrive/Pictures/random/g_icon.ico")
r.resizable(False,False)

canvas = tk.Canvas(r, height= 900, width= 1300,bg ="white")
canvas.place(x=-5,y=-5)


# ------------------- L O G O -------------------
g = tk.Label(r, text="G",font=("sans-serif",60),height=1,fg="dodgerblue3",bg ="white")
g.place(x= 281, y = 30)
o = tk.Label(r, text="o",font=("sans-serif",60),height=1,fg="firebrick1",bg ="white")
o.place(x= 340, y = 30)
o2 = tk.Label(r, text="o",font=("sans-serif",60),height=1,fg="gold1",bg ="white")
o2.place(x= 385, y = 30)
g2 = tk.Label(r, text="g",font=("sans-serif",60),height=1,fg="dodgerblue3",bg ="white")
g2.place(x= 430, y = 30)
l = tk.Label(r, text="l",font=("sans-serif",60),height=1,fg="forestgreen",bg ="white")
l.place(x= 473, y = 30)
e= tk.Label(r, text="e",font=("sans-serif",60),height=1,fg="firebrick1",bg ="white")
e.place(x= 490, y = 30)


# ------------------- T E X T ' S -------------------
label2 = tk.Label(r, text="SEARCH :", width= 15,font= ("san-serif",9,"bold"),bg="white",fg="black")
label2.place(x = 151, y= 130)

label3 = tk.Label(r, text="Language : English", width= 15,font= ("san-serif",8,"bold"),bg="white",fg="black")
label3.place(x = 360, y= 164)


# ------------------- I N P U T / O U T P U T -------------------
input = Entry(r, width=50,bg="white",font= ("arial",9,"bold"),fg="black")
input.place(x = 240, y=130)

output = tk.Text(r,wrap=WORD, width= 75,height=9,font= ("sans-serif",9,"bold"),bg="white",fg="black")
output.place(x = 151, y= 200)


# ------------------- S E A R C H _ F U N C T I O N -------------------
def click():
    entered_text= (input.get()).lower()
    output.delete(0.0, END)
    try:
        definition = dictionary[entered_text]
    except:
        definition = "Sorry there's no such word in our Library. Use other app or website"
    output.insert(END, definition)


# ------------------- S E A R C H _ B U T T O N -------------------
search = tk.Button(r, text="🔍",font= "hamlin",bg="orange4",fg="black",bd=5,command=click)
search.place(x = 600, y= 124)


# ------------------- D I C T I O N A R Y -------------------
dictionary= {'python':
             'Python is a computer programming language often used to build websites and software, automate tasks, and conduct data analysis. '
              ,
             'java':
             'Java is an object-oriented programming language that produces software for multiple platforms.'
              ,
             'robin':
             'An 18 year old handsome programmer '
              ,
             'programming':
             'Programming is the process of creating a set of instructions that tell a computer how to perform a task.'
              ,
             'programming languanges':
             'Programming can be done using a variety of computer programming languages, such as JavaScript, Python, and C++.'
              ,
             'jennie kim':
             'Jennie Kim (Korean: 김제니; born January 16, 1996),\nknown mononymously as Jennie, is a South Korean singer and rapper.\n\nWife of mine'
              ,
             'dog':
             'The dog or domestic dog, (Canis familiaris or Canis lupus familiaris) is a domesticated descendant of the wolf which is characterized by an upturning tail.'
             ,
             'schedule':
             'Monday\t\tTuesday\t\tWednesday\t\tThursday\t\tFriday\t\t'+
             '\n7-10-CHEM\t\t7-10-PLD\t\t7-10-CHEM\t\t7-10-PLD\t\t8-9-CPED\t\t'+
             '\n10-11:30-MMW\t\t10-11:30-STS\t\t10-11:30-MMW\t\t10-11:30-STS\t\t'+
             '\n\n1-3-PE\t\t12:30-2-CALC\t\t\t\t12:30-2-CALC'
             }


# ------------------- D E V E L O P E R -------------------
label_dev = tk.Label(r, text="by RobinDelaCruz", width= 15,font= ("san-serif",7),bg="white",fg="black")
label_dev.place(x= 705, y=381)

label_p = tk.Label(r, text="Philippines 2021©", width= 15,font= ("san-serif",7),bg="white",fg="black")
label_p.place(x= 0, y=381)


# ------------------- T H E M E _ F U N C T I O N -------------------
def select():
    if theme.get() == 1:
        canvas.config(bg = "gray17")
        label2.config(bg="gray17",fg="white")
        label3.config(bg="gray17",fg="white")
        g.config(bg="gray17")
        o.config(bg="gray17")
        o2.config(bg="gray17")
        g2.config(bg="gray17")
        l.config(bg="gray17")
        e.config(bg="gray17")
        label_dev.config(bg="gray17",fg="white")
        label_p.config(bg="gray17",fg="white")
        light.config(bg="gray17",fg="white",text="Light Mode")

    else:
        canvas.config(bg="white")
        label2.config(bg="white",fg="black")
        label3.config(bg="white",fg="gray17")
        g.config(bg="white")
        o.config(bg="white")
        o2.config(bg="white")
        g2.config(bg="white")
        l.config(bg="white")
        e.config(bg="white")
        label_dev.config(bg="white",fg="black")
        label_p.config(bg="white",fg="black")
        light.config(fg="gray17",bg="white",text="Dark Mode")

theme = IntVar()

# ------------------- T H E M E -------------------
light = tk.Checkbutton(r, text="Dark Mode",width=8, font= ('Arial', 7, 'bold'),fg="black",bg = "white",variable=theme,command=select)
light.place(x=20, y=18)

r.mainloop()