from tkinter import *
def action():
    window = Tk()
    window.geometry('300x300')
    e=Entry(window,width=56,borderwidth=5)
    e.place(x=10,y=80)
    f = Entry(window, width=56, borderwidth=5)
    f.place(x=10,y=10)
    def click():
        #l.place_forget()
        l.destroy()
    def anagram():
        global l
        user_input = e.get()
        user1_input = f.get()
        s1 = str(user_input)
        s2 = str(user1_input)
        window.update_idletasks()
        if(sorted(s1)==sorted(s2)):
            l=Label(window,text="Two Strings are Anagram")
            l.place(x=10,y=200)
        else:
            l=Label(window,text="Two Strings are not an Anagram")
            l.place(x=10, y=200)


    b = Button(window, text='Check',command=anagram)
    b.place(x=20, y=120)
    b = Button(window, text='Try Another', command=click)
    b.place(x=100, y=120)
    window.mainloop()