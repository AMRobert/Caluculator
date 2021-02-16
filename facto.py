from tkinter import *
def action():
    window = Tk()
    window.geometry('300x300')
    e=Entry(window,width=56,borderwidth=5)
    e.place(x=10,y=80)
    def click():
        #l.place_forget()
        l.destroy()
    def facto():
        global l
        user_input = e.get()
        num = str(user_input)
        num = int(num)
        fact = 1
        window.update_idletasks()

        if num<0:
            l=Label(window, text="Please Enter a Positive Number, Factorial doesn't exists for negative numbers")
            l.place(x=10,y=200)
        elif num==0:
            l = Label(window, text="Factorial of 0 is 1")
            l.place(x=10, y=200)
        else:
            for i in range(1,num+1):
                fact = fact * i
            l = Label(window, text="Factorial of "+str(num)+" is "+str(fact))
            l.place(x=10, y=200)
    b = Button(window, text='Check',command=facto)
    b.place(x=20, y=120)
    b = Button(window, text='Try Another', command=click)
    b.place(x=100, y=120)
    window.mainloop()