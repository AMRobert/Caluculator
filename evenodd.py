from tkinter import *
def action():
    window = Tk()
    window.geometry('300x300')
    e=Entry(window,width=56,borderwidth=5)
    e.place(x=10,y=80)
    def click():
        #l.place_forget()
        l.destroy()
    def evenodd():
        global l
        user_input = e.get()
        s1 = str(user_input)
        s1 = int(s1)
        #s1 = int(s1)
        window.update_idletasks()
        if(s1%2==0):
            l=Label(window, text=str(s1) + " is an Even Number")
            l.place(x=10,y=200)
        elif(s1==0):
            l = Label(window, text=str(s1) + " is an Even Number")
            l.place(x=10, y=200)
        else:
            l = Label(window, text=str(s1) + " is an Odd Number")
            l.place(x=10, y=200)

    b = Button(window, text='Check',command=evenodd)
    b.place(x=20, y=120)
    b = Button(window, text='Try Another', command=click)
    b.place(x=100, y=120)
    window.mainloop()