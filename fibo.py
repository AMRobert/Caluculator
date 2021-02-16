from tkinter import *
def action():
    window = Tk()
    window.geometry('300x300')
    e=Entry(window,width=56,borderwidth=5)
    e.place(x=10,y=80)
    def click():
        #l.place_forget()
        l.destroy()
    def fibo():
        global l
        user_input = e.get()
        terms = str(user_input)
        terms = int(terms)
        n1, n2 =0, 1
        window.update_idletasks()

        if terms<=0:
            l=Label(window, text="Please Enter a Positive Number")
            l.place(x=10,y=200)
        elif terms==1:
            l = Label(window, text="Fibonacci Series"+str(terms)+":"+str(n1))
            l.place(x=10, y=200)
        else:

            count = 0
            while count<terms:
                res = n1 + n2
                n1 = n2
                n2 = res
                count+=1
            l = Label(window, text="Fibonacci Series of "+str(terms)+" is "+str(res))
            l.place(x=10, y=200)
    b = Button(window, text='Check',command=fibo)
    b.place(x=20, y=120)
    b = Button(window, text='Try Another', command=click)
    b.place(x=100, y=120)
    window.mainloop()