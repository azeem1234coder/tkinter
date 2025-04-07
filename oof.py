from tkinter import *
from datetime import date
root = Tk()
root.title('Getting Started with Widgets')
root.geometry ('400x300')
lbl =Label(text="Hey There!", fg="white", bg="#672F5F", height=1, width=300)
name_1b1 =Label (text= "Full Name", bg="blue")
name_entry = Entry()
def display():
    name= name_entry.get()
    global message
    message = "Welcome to the Application! \nToday's date is: "
    greet = "Hello" +name+"\n"
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())
text_box= Text(height=3)
btn =Button(text="Begin", command=display, height= 1, bg="#1261A8", fg= "white")
lbl.pack()
name_1b1.pack()
name_entry.pack()
btn.pack()
text_box.pack()
root.mainloop()