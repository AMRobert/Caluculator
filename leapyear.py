from tkinter import *
def action():
    window = Tk()
    window.geometry('300x300')
    e=Entry(window,width=56,borderwidth=5)
    e.place(x=10,y=80)
    def click():
        #l.place_forget()
        l.destroy()
    def leapyear():
        global l
        user_input = e.get()
        s1 = str(user_input)
        s1 = int(s1)
        #s1 = int(s1)
        window.update_idletasks()
        if((s1%4==0 and s1%100!=0) or s1%400==0):
            l=Label(window, text=str(s1) + " is an Leap Year")
            l.place(x=10,y=200)
        else:
            l = Label(window, text=str(s1) + " is not an Leap Year")
            l.place(x=10, y=200)

    b = Button(window, text='Check',command=leapyear)
    b.place(x=20, y=120)
    b = Button(window, text='Try Another', command=click)
    b.place(x=100, y=120)
    window.mainloop()