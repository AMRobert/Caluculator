from tkinter import *
def action():
    window = Tk()
    window.geometry('300x300')
    e=Entry(window,width=56,borderwidth=5)
    e.place(x=10,y=80)
    def click():
        #l.place_forget()
        l.destroy()
    def ascii():
        global l
        user_input = e.get()
        s1 = str(user_input)
        #s1 = int(s1)
        window.update_idletasks()
        res = ord(s1)
        l=Label(window, text="The ASCII Value of " +s1+ " is " +str(res))
        l.place(x=10,y=200)


    b = Button(window, text='Check',command=ascii)
    b.place(x=20, y=120)
    b = Button(window, text='Try Another', command=click)
    b.place(x=100, y=120)
    window.mainloop()