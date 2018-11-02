Hi I'm trying to do an assignment and I'm having a problem inserting information into mysql database.

How it should work: The information should be written in the blank areas { Entry1 and Entry2} and then when hit ENTER it should go to the database and be stored.

The first problem I'm having is that I don't know how to write or implement the code for the file "GUINeW" to "MYSQL2" so the information could be stored in the database.

Secondly is that I'm getting "No module named 'mysql'" in both of my scripts, which resides in pictures number 9 and 10. 








from tkinter import *
from tkinter import messagebox



window = Tk()
window.geometry("640x480")


# Yellow
y0 = Label(window, bg = "Yellow", fg = "Black", width = 320, height = 1, text = "MENU")
y0.grid(row = 1, column = 2) # Red(Left) + Purple(Right) are Columns


def getEntry1(key):

   r111 = r1.get()
   print(r111)
   r112 = r2.get()
   print(r112)
   r113 = r3.get()
   print(r113)
   r114 = r4.get()
   print(r114)
   r115 = r5.get()
   print(r115)
   r116 = r6.get()
   print(r116)
   r117 = r7.get()
   print(r117)
   r118 = r8.get()
   print(r118)
   r119 = r9.get()
   print(r119)


# Red Frame with 1 Label och 9 Entrys.
r11 = Frame(window, bg = "Red", width = 320, height = 640)
r0 = Label(r11, bg = "Red", fg = "White", text = "1. You will get punked!", padx = 60, pady = 15)
r1 = Entry(r11, bg = "Red", fg = "White")
r1.bind("<Return>", getEntry1)
r2 = Entry(r11, bg = "Red", fg = "White")
r2.bind("<Return>", getEntry1)
r3 = Entry(r11, bg = "Red", fg = "White")
r3.bind("<Return>", getEntry1)
r4 = Entry(r11, bg = "Red", fg = "White")
r4.bind("<Return>", getEntry1)
r5 = Entry(r11, bg = "Red", fg = "White")
r5.bind("<Return>", getEntry1)
r6 = Entry(r11, bg = "Red", fg = "White")
r6.bind("<Return>", getEntry1)
r7 = Entry(r11, bg = "Red", fg = "White")
r7.bind("<Return>", getEntry1)
r8 = Entry(r11, bg = "Red", fg = "White")
r8.bind("<Return>", getEntry1)
r9 = Entry(r11, bg = "Red", fg = "White")
r9.bind("<Return>", getEntry1)


def getEntry2(key):

    p111 = p1.get()
    print(p111)
    p112 = p2.get()
    print(p112)
    p113 = p3.get()
    print(p113)
    p114 = p4.get()
    print(p114)
    p115 = p5.get()
    print(p115)
    p116 = p6.get()
    print(p116)
    p117 = p7.get()
    print(p117)
    p118 = p8.get()
    print(p118)
    p119 = p9.get()
    print(p119)


# Purple Frame with 1 label and 9 Entrys.
p11 = Frame(window, bg = "Purple", width = 320, height = 640)
p0 = Label(p11, bg = "Purple", fg = "White", text = "What games do you play?", padx = 60, pady = 15)
p1 = Entry(p11, bg = "Purple", fg = "White")
p1.bind("<Return>", getEntry2)
p2 = Entry(p11, bg = "Purple", fg = "White")
p2.bind("<Return>", getEntry2)
p3 = Entry(p11, bg = "Purple", fg = "White")
p3.bind("<Return>", getEntry2)
p4 = Entry(p11, bg = "Purple", fg = "White")
p4.bind("<Return>", getEntry2)
p5 = Entry(p11, bg = "Purple", fg = "White")
p5.bind("<Return>", getEntry2)
p6 = Entry(p11, bg = "Purple", fg = "White")
p6.bind("<Return>", getEntry2)
p7 = Entry(p11, bg = "Purple", fg = "White")
p7.bind("<Return>", getEntry2)
p8 = Entry(p11, bg = "Purple", fg = "White")
p8.bind("<Return>", getEntry2)
p9 = Entry(p11, bg = "Purple", fg = "White")
p9.bind("<Return>", getEntry2)


def pushButton1():

    messagebox.showwarning("Hello", "Game Over")


def pushButton2():

    messagebox.showinfo("Hello", "Punked")



o = Button(r11, bg = "White", text = "Options", fg = "Green", command = pushButton2)
g = Button(p11, bg = "White", text = "Game Over", fg = "Orange", command = pushButton1)



# Yellow
y0.pack(side = TOP) # Label MENU, Upper Column


# Buttons
o.pack(side = BOTTOM) # Button Option
g.pack(side = BOTTOM) # Button Game Over


# Red
r11.pack_propagate(False)
r11.pack(side = LEFT)
r0.pack()
r1.pack()
r2.pack()
r3.pack()
r4.pack()
r5.pack()
r6.pack()
r7.pack()
r8.pack()
r9.pack()


# Purple
p11.pack_propagate(False)
p11.pack(side = RIGHT)
p0.pack()
p1.pack()
p2.pack()
p3.pack()
p4.pack()
p5.pack()
p6.pack()
p7.pack()
p8.pack()
p9.pack()





# Den loopar / är på tills den stängs av.
window.mainloop()


