from tkinter import *
def action():
    window = Tk()
    window.geometry('300x300')
    e=Entry(window,width=56,borderwidth=5)
    e.place(x=10,y=10)
    def click():
        #l.place_forget()
        l.destroy()
    def palindrome():
        global l
        user_input = e.get()
        n = str(user_input)
        window.update_idletasks()
        if n == n[::-1]:
            l=Label(window,text="This is palindrome")
            l.place(x=100,y=100)
        else:
            l=Label(window,text="This is not palindrome")
            l.place(x=100,y=100)


    b = Button(window, text='Check',command=palindrome)
    b.place(x=40,y=60)
    b = Button(window,text='Try Another',command=click)
    b.place(x=140,y=60)
    window.mainloop()
