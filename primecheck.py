from tkinter import *
def action():
    window = Tk()
    window.geometry('300x300')
    e=Entry(window,width=56,borderwidth=5)
    e.place(x=10,y=80)
    def isPrime(num):
        if num<2:
            return False
        if num==2:
            return True
        for i in range(3,(num//2)+1):

            if num%i==0:
                return False
        else:
            return True
    def click():
        #l.place_forget()
        l.destroy()
    def PrimeNumber():
        global l
        user_input = e.get()
        num = str(user_input)
        num = int(num)
        window.update_idletasks()
        val = isPrime(num)
        if val==True:
            l = Label(window, text=str(num)+" is a Prime Number")
            l.place(x=10, y=200)

        else:
            l = Label(window, text=str(num)+" is not a Prime Number")
            l.place(x=10, y=200)





    b = Button(window, text='Check',command=PrimeNumber)
    b.place(x=20, y=120)
    b = Button(window, text='Try Another', command=click)
    b.place(x=100, y=120)
    window.mainloop()

